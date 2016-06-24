# coding: utf-8
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import F
from django.forms import formset_factory
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from KIF.models import Drug, RecordPatient, Patient, Department
from pharmacy.forms import SheetAssignmentForm, EditStockTackingFormset, UseDrugForPatientForm
from pharmacy.models import StockTacking, AcceptanceList, AppointmentList


class GetAllDrugs(ListView):
    model = Drug
    template_name = "admin_pharmacy.html"

    #
    # @login_required(login_url=reverse_lazy('login-doctor'))
    # def dispatch(self, request, *args, **kwargs):
    #     return super(GetAllDrugs, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GetAllDrugs, self).get_context_data(**kwargs)
        context['drugs'] = Drug.objects.all()
        context['count'] = Drug.objects.count()
        return context


@csrf_exempt
def AjaxPostDrugCreate(request):
    if request.is_ajax():
        id_drug = request.POST.getlist('id[]')
        count_drug = request.POST.getlist('count[]')
        doctor_id = request.session.get('doctor_id')
        dataStockTackingExsist = StockTacking.objects.filter(date__date=datetime.today())
        if dataStockTackingExsist:
            return JsonResponse({"data": "Добавлять медикаменты можно только один раз в день"})
        else:
            for idDrug, countDrug in zip(id_drug, count_drug):
                StockTacking.objects.bulk_create(
                    [StockTacking(drugSt_id=idDrug, date=datetime.now(), amount=countDrug, rest=countDrug,
                                  doctor_id=doctor_id)])
            return JsonResponse({"data": "Успешно выполнено!"})
    else:
        return HttpResponseRedirect(reverse('admin-pharmacy'))


@login_required(login_url=reverse_lazy('login-doctor'))
def SheetAssignmentView(request):
    patient = RecordPatient.objects.filter(issue_date__isnull=True)
    error = ""
    if request.method == 'POST':
        if request.POST['action'] == "+":
            extra = int(float(request.POST['extra'])) + 1
            formset = formset_factory(SheetAssignmentForm, extra=extra)
        elif request.POST['action'] == "-":
            if int(float(request.POST['extra'])) - 1 >= 0:
                extra = int(float(request.POST['extra'])) - 1
                formset = formset_factory(SheetAssignmentForm, extra=extra)
            else:
                extra = 0
                formset = formset_factory(SheetAssignmentForm, extra=extra)
        else:
            extra = int(float(request.POST['extra']))
            patientID = int(request.POST['patient'])
            formset = formset_factory(SheetAssignmentForm, extra=extra)(request.POST)
            if request.POST['action'] == "Create":
                if formset.is_valid():
                    try:
                        doctor_id = request.session.get('doctor_id')
                        for form_c in formset:
                            instance = form_c.save(commit=False)
                            instance.patient_id = patientID
                            instance.doctor_id = doctor_id
                            instance.beginAppointment = datetime.now()
                            instance.save()
                        return HttpResponseRedirect(reverse('sheet-assignment'))
                    except:
                        error = "Error"

    else:
        extra = 1
        formset = formset_factory(SheetAssignmentForm, extra=extra)

    context = {
        "formset": formset,
        "extra": extra,
        "doctor_id": request.session.get('doctor_id'),
        "patient": patient,
        'title': "Лист назначения",
        "error": error

    }

    return render(request, "sheet_assignment.html", context)


def EditStockTackingView(request):
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        formset = EditStockTackingFormset(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        datasStockTakingExist = StockTacking.objects.filter(date__date=datetime.today())
        if datasStockTakingExist:
            formset = EditStockTackingFormset(queryset=StockTacking.objects.filter(date__date=datetime.today()))
        else:
            return HttpResponseRedirect(reverse('admin-pharmacy-drug-create'))
    args['formset'] = formset
    return render_to_response('edit_admin_pharmacy.html', args)


@csrf_exempt
def AjaxDrugForPatient(request):
    if request.is_ajax():
        patient = request.GET.get('patient_id', '')
        if patient:
            appointment = AppointmentList.objects.filter(patient=patient).values_list('drugAl__id', 'drugAl__name_drug')
            context = {
                "appointment_data": dict(appointment)
            }
            return JsonResponse(context)

    else:
        raise Http404


@csrf_exempt
def AjaxDrugReportForPatient(request):
    if request.is_ajax():
        drugToDate = request.POST.get('date_to_drug', '')
        if drugToDate:
            get_drug = StockTacking.objects.filter(date__date=drugToDate).values_list(
                'drugSt__name_drug',
                'amount')
            context = {
                "report_drug": dict(get_drug)
            }
            return JsonResponse(context)

    else:
        raise Http404


@csrf_exempt
def AjaxDrugReportRangeDateForPatient(request):
    if request.is_ajax():
        drug = request.POST.get('drug', '')
        drugToDate = request.POST.get('date_to_drug', '')
        drugFromDate = request.POST.get('date_from_drug', '')
        if drug and drugToDate:
            get_drug = StockTacking.objects.filter(drugSt=drug, date__range=(drugToDate, drugFromDate)).values_list(
                'date',
                'amount')
            context = {
                "report_drug": {str(k): v for k, v in dict(get_drug).items()}
            }
            return JsonResponse(context)

    else:
        raise Http404


def UseDrugForPatientView(request):
    args = {}
    args.update(csrf(request))
    patient = RecordPatient.objects.filter(issue_date__isnull=True)
    args['patient'] = Patient.objects.filter(id__in=patient.values('patient_fk'))
    l = AppointmentList.objects.filter(patient__in=patient).values('patient').distinct()
    args['l'] = Patient.objects.filter(id__in=l)
    args['appointmentListfilter'] = l

    if request.method == "POST":
        form = UseDrugForPatientForm(request.POST)
        count = request.POST.get('amount', '')
        id_drug = request.POST.get('appointmentList', '')
        id_patient = request.POST.get('patientToView', '')
        # date = request.POST.get('acceptDate', '')
        count_drug_postup = StockTacking.objects.filter(drugSt__id=int(id_drug), date__date=datetime.today())
        numdrug = AppointmentList.objects.get(drugAl=int(id_drug), patient=id_patient)

        a = AcceptanceList.objects.values_list('amount').filter(appointmentList=numdrug.id,
                                                                acceptDate__date=datetime.today())

        s = sum([sum(x) for x in zip(*a)])

        if s + int(count) <= numdrug.amount:
            if count_drug_postup.values('rest'):
                countDrug_toList = count_drug_postup.values_list('rest', flat=True)
                if countDrug_toList[0] - int(count) >= 0:
                    StockTacking.objects.filter(drugSt__id=int(id_drug), date__date=datetime.today()).update(
                        rest=F('rest') - count)
                    if form.is_valid():
                        instance = form.save(commit=False)
                        instance.appointmentList = numdrug
                        instance.acceptDate = datetime.today()
                        instance.save()
                    messages.success(request, 'Успешно')
                else:
                    messages.error(request, '1')
                    args["error"] = "Недостаточное количество лекарств"
            else:
                messages.error(request, '2')
                args["error"] = "Лекартсво не поступили, ждите ...."
        else:
            messages.error(request, '3')
            args["error"] = "Пациент выпил нужное количество лекарств"
    else:
        form = UseDrugForPatientForm()
    args["form"] = form
    args['title2'] = request.session.get('doctor_id')

    return render_to_response("use_drug_for_patient.html", args)


class ShowAllDrugReportForDoctor(ListView):
    template_name = "report/show_drug_report.html"
    model = StockTacking

    def get_context_data(self, **kwargs):
        context = super(ShowAllDrugReportForDoctor, self).get_context_data(**kwargs)
        drug = Drug.objects.all()
        context['reportDrug'] = drug
        context['title'] = "Медикаменты"

        return context


class ShowEatDrugReport(ListView):
    template_name = "report/show_eat_drug_reporpt.html"
    model = Department

    def get_context_data(self, **kwargs):
        context = super(ShowEatDrugReport, self).get_context_data(**kwargs)
        department = Department.objects.all()
        context['department'] = department

        return context


@csrf_exempt
def GetAjaxRecordPatient(request):
    if request.is_ajax():
        department_id = request.POST.get('dept_id', '')
        if department_id:
            record_patient = RecordPatient.objects.filter(dept_fk=department_id).values_list("id",
                                                                                             "patient_fk__surname_pat",
                                                                                             "patient_fk__name_pat",
                                                                                             "patient_fk__last_name_pat"
                                                                                             )
            id_pat = record_patient.values_list('id', flat=True)
            surname = record_patient.values_list('patient_fk__surname_pat', flat=True)
            name = record_patient.values_list("patient_fk__name_pat", flat=True)
            lastname = record_patient.values_list("patient_fk__last_name_pat", flat=True)

            if id_pat:
                fio_patient = []
                id_patient = []
                for i in range(len(id_pat)):
                    fio_patient.append(surname[i] + " " + name[i] + " " + lastname[i])
                    id_patient.append(id_pat[i])
                dictionary = dict(zip(id_patient, fio_patient))
                return JsonResponse({"record_patient_id": dictionary})
            else:
                return JsonResponse({"record_patient_id": dict()})

    else:
        raise Http404


class DetailShowEatDrugReport(ListView):
    template_name = "report/show_eat_drug_reporpt.html"
    model = Department

    def get_context_data(self, **kwargs):
        context = super(DetailShowEatDrugReport, self).get_context_data(**kwargs)
        department = Department.objects.all()
        context['department'] = department
        context['alllll'] = AcceptanceList.objects.filter(appointmentList=self.kwargs['pk'])
        return context
