# coding: utf-8
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView

from Analyze.models import GenBloodAnalyse
from KIF.forms import LoginForm, PasswordChangeForm
from KIF.models import Patient, RecordPatient
from pharmacy.models import AppointmentList
from profileUser.forms import UpdateProfileInfo


class ProfileInfo(DetailView):
    template_name = 'profileInfo.html'
    model = Patient

    def get(self, request, *args, **kwargs):
        try:
            patient_id = request.session.get('patient')
            patient_info = Patient.objects.get(id=patient_id)
            record_patient = RecordPatient.objects.get(id=patient_info.id)
            context = {
                'patient': patient_info,
                'record': record_patient
            }
            return self.render_to_response(context)
        except Patient.DoesNotExist:
            return HttpResponseRedirect(reverse('login'))
        except RecordPatient.DoesNotExist:
            return HttpResponseRedirect(reverse('thanks'))

    def get_context_data(self, **kwargs):
        context = super(ProfileInfo, self).get_context_data(**kwargs)

        context['gen_analyze_blood'] = GenBloodAnalyse.objects.all()
        return context


class UpdatePatientInfo(UpdateView):
    model = Patient
    form_class = UpdateProfileInfo
    template_name = 'updateProfile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('patient'):
            return HttpResponseRedirect(reverse('login'))
        else:
            return super(UpdatePatientInfo, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        patient_id = self.request.session.get('patient')
        obj = Patient.objects.get(id=patient_id)
        return obj

    def get_success_url(self):
        login_or_pass_change = int(self.request.POST.get('login-password-change', '0'))
        if login_or_pass_change > 0:
            del self.request.session['patient']
            return reverse('login')
        else:
            messages.success(self.request, "Successfully updated")
            return reverse('updateInfo')


class LoginPatient(FormView):
    model = Patient
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']
        try:
            record = Patient.objects.get(login_pat=login, password_pat=password)
            if record:
                self.request.session.set_expiry(4000)
                self.request.session['patient'] = record.id
                name_patient = "%s %s" % (record.surname_pat, record.name_pat)
                self.request.session['patient_name'] = name_patient
                return HttpResponseRedirect(reverse('home'))
        except Patient.DoesNotExist:
            context = {
                'form': self.form_class,
                'errors': "Введите корректные данные"
            }
            return render(self.request, self.template_name, context)


class LogoutPatient(DeleteView):
    def get(self, request, *args, **kwargs):
        try:
            if request.session.get('patient'):
                del request.session['patient']
        except Http404:
            pass
        return HttpResponseRedirect(reverse("login"))


class ChangePassword(FormView):
    template_name = 'changePassword.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            patient_login = Patient.objects.get(email_pat=email)
            subject = "You password is change"
            message = "You password is: " + str(patient_login.password_pat)
            to_list = [patient_login.email_pat, ]
            send_mail(subject, message, settings.EMAIL_HOST_USER, to_list, fail_silently=True)
            return HttpResponseRedirect(reverse('thanks'))
        except Patient.DoesNotExist:
            context = {
                'errors': "Вы ввели неправильные данные, все данные регистрозависимые",
                'form': self.form_class
            }
            return render(self.request, self.template_name, context)


def thank_view(request):
    return render_to_response('thanks.html', context_instance=RequestContext(request))


class AppointmentListReport(ListView):
    model = AppointmentList
    template_name = "report_appointment_list_patient.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('patient'):
            return HttpResponseRedirect(reverse('login'))
        else:
            return super(AppointmentListReport, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AppointmentListReport, self).get_context_data(**kwargs)
        session_patient = self.request.session.get('patient')
        patient_id = Patient.objects.get(id=session_patient)
        record_patient = RecordPatient.objects.get(patient_fk=patient_id)
        app_list = AppointmentList.objects.filter(patient=record_patient.id)
        context['appreportinfo'] = app_list
        return context
