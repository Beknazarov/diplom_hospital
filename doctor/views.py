# coding: utf-8
from django.contrib import messages
from django.contrib.auth import (
    login as auth_login, logout as auth_logout)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from KIF.models import Doctor, Patient, RecordPatient


class LoginView(FormView):
    template_name = "authenticate_doctor.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()

        auth_login(self.request, user)
        get_status = Doctor.objects.filter(loginDoc=form.get_user())

        status = list(get_status.values_list("role_doc", flat=True))  # роли
        if status:
            doctor_id = int(list(get_status.values_list("id", flat=True))[0])
            self.request.session['doctor_id'] = doctor_id
            if status[0] == 2:  # 2 - доктор
                self.request.session['doctorRole'] = status[0]
                return HttpResponseRedirect(reverse('sheet-assignment'))
            elif status[0] == 3:  # 3 - фармацевт
                self.request.session['doctorRole'] = status[0]
                return HttpResponseRedirect(reverse('admin-pharmacy-drug-create'))
            else:
                messages.error(self.request, "Введите корректные данные")
                return HttpResponseRedirect(reverse('login-doctor'))
        else:
            messages.error(self.request, "Введите корректные данные")
            return HttpResponseRedirect(reverse('login-doctor'))


class LogoutView(LoginRequiredMixin, RedirectView):
    permanent = False
    url = reverse_lazy('login-doctor')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, args, kwargs)


class AdminLoginView(FormView):
    template_name = "admin/login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        username_doctor = self.request.GET.get('username', '')
        password_doctor = self.request.GET.get('password', '')
        if username_doctor and password_doctor:
            user = User.objects.get(username=username_doctor)
            if user.check_password(password_doctor):
                status = dict(Doctor.objects.filter(loginDoc=user).values_list('id', 'role_doc'))
                if status:
                    self.request.session['doctor_role'] = status.values()[0]
                else:
                    print("error session print")
        return super(AdminLoginView, self).form_valid(form)


def AjaxGetDoctorStatus(request):
    if request.is_ajax():
        username_doctor = request.GET.get('username', '')
        password_doctor = request.GET.get('password', '')
        if username_doctor and password_doctor:
            user = User.objects.get(username=username_doctor)
            # auth_login(self.request, user)
            if user.check_password(password_doctor):
                status = dict(Doctor.objects.filter(loginDoc=user).values_list('id', 'role_doc'))
                # if status:
                #     request.session['doctor_role'] = status.values()[0]
                # response = redirect(self.request, '/')
                # response.set_cookie(key='doctor_role', value=status.values()[0])
                # print(self.request.COOKIES.get('doctor_role'))
                return JsonResponse({"data": "success"})
    else:
        raise Http404


@csrf_exempt
def GetDoctorInfo(request):
    if request.is_ajax():
        doctor_id = request.POST.get('doctor_id')
        if doctor_id:
            doctor = Doctor.objects.filter(id=doctor_id).values_list('id', 'fio_doc')
            return JsonResponse({"infoDoc": dict(doctor)})
    else:
        raise Http404


class DoctorAttendingPatient(ListView):
    template_name = "showAllPatientAttending.html"
    model = RecordPatient

    def dispatch(self, request, *args, **kwargs):
        doctor_id = self.request.session.get('doctor_id')
        if not doctor_id:
            return HttpResponseRedirect(reverse('login-doctor'))
        else:
            return super(DoctorAttendingPatient, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DoctorAttendingPatient, self).get_context_data(**kwargs)
        doctor_id = self.request.session.get('doctor_id')
        record_patient = RecordPatient.objects.filter(doctor=doctor_id)
        context['rpatient'] = record_patient
        return context


class DoctorMedCartPrint(DetailView):
    template_name = 'printMedKarta.html'
    model = Patient

    def get(self, request, *args, **kwargs):
        try:
            record_patient = RecordPatient.objects.get(id=self.kwargs['pk'])
            patient_info = Patient.objects.get(id=record_patient.patient_fk.id)

            context = {
                'patient': patient_info,
                'record': record_patient
            }
            return self.render_to_response(context)
        except Patient.DoesNotExist:
            return HttpResponseRedirect(reverse('login'))
        except RecordPatient.DoesNotExist:
            return HttpResponseRedirect(reverse('thanks'))
#
#
# class DoctorAdminMedCartPrint(DetailView):
#     template_name = "admin/preferences/preferences.html"
#     model = Patient
#
#     def get(self, request, *args, **kwargs):
#         try:
#             record_patient = RecordPatient.objects.get(id=1)
#             patient_info = Patient.objects.get(id=record_patient.patient_fk.id)
#
#             context = {
#                 'patient': patient_info,
#                 'record': record_patient
#             }
#             return self.render_to_response(context)
#         except Patient.DoesNotExist:
#             return HttpResponseRedirect(reverse('login'))
#         except RecordPatient.DoesNotExist:
#             return HttpResponseRedirect(reverse('thanks'))
