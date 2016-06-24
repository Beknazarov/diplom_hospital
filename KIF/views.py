# coding:utf-8
from django.http.response import Http404, JsonResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from KIF.models import Region, Town, RecordPatient, Diagnosis, TypeOperation


class AjaxForGetRegion(ListView):
    def get(self, request, *args, **kwargs):

        if request.is_ajax():
            area_id = request.GET.get('area_id', '')
            if area_id:
                region = Region.objects.filter(area_fk=int(area_id)).values_list('id', 'name_reg')
                context = {
                    "region": dict(region)
                }
                return JsonResponse(context)

        else:
            raise Http404


class AjaxForGetTown(ListView):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            region_id = request.GET.get('region_id', '')
            if region_id:
                town = Town.objects.filter(region_fk=int(region_id)).values_list('id', 'name_town')
                context = {
                    "town": dict(town)
                }

                return JsonResponse(context)
        else:
            raise Http404


class InfoTable(ListView):
    template_name = "tableInfo.html"
    model = RecordPatient

    # @method_decorator(login_required(login_url='/admin/'))
    # def dispatch(self, *args, **kwargs):
    #     return super(InfoTable, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InfoTable, self).get_context_data(**kwargs)

        patient = RecordPatient.objects.filter(issue_date__isnull=True)
        diagnose = Diagnosis.objects.filter(patient_fk__in=patient.values('id'))
        context['diagnose'] = diagnose
        operation = TypeOperation.objects.filter(status_tpop="process").select_related()

        context['operation'] = operation
        operation_diagnose = Diagnosis.objects.filter(patient_fk__in=operation.values('patient_fk__id'))
        context['operation_diagnose'] = operation_diagnose
        return context


class TemplateDoctorView(TemplateView):
    template_name = "base_doctor.html"
