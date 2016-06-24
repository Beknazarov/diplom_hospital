# coding=utf-8
import cStringIO
from itertools import chain
import xhtml2pdf.pisa as pisa
from django.db.models.lookups import Exact
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template

from KIF.models import RecordPatient, Patient
from hospital import settings
from medicalhistory.models import HistoryPatientLife, Women, PatientConditionsNow,Senses,RespiratorySystem, CardiovascularSystem, \
    GenitoUrinarySystem, EndocrineSystem, NeuroPsychologicalSystem, StatusLocalis, DigestiveSystem


def get_context():
    context = {}
    try:

        record = RecordPatient.objects.get(patient_fk_id=1)
        patient = Patient.objects.get(id=record.patient_fk_id)
        context['patient']=patient
        context['record']=record
        historylife = HistoryPatientLife.objects.get(recordpatient=record)
        # if(patient.gender_pat==patient.FEMALE):
        #
        #     context['womenstatus']=False
        # else:
        #     context['womenstatus']=True
        context['women'] = Women.objects.get(history=historylife.pk)
        context['history_patient_life'] = historylife
        context['patient_conditions_now'] = PatientConditionsNow.objects.get(history=historylife.pk)
        context['senses'] = Senses.objects.get(history=historylife.pk)
        context['respiratory_system'] = RespiratorySystem.objects.get(history=historylife.pk)
        context['cardiovascular_system'] = CardiovascularSystem.objects.get(history=historylife.pk)
        context['digestive_system'] = DigestiveSystem.objects.get(history=historylife.pk)
        context['genito_urinary_system'] = GenitoUrinarySystem.objects.get(history=historylife.pk)
        context['endocrine_system'] = EndocrineSystem.objects.get(history=historylife.pk)
        context['neuro_psychological_system'] = NeuroPsychologicalSystem.objects.get(history=historylife.pk)
        context['status_localis'] = StatusLocalis.objects.get(history=historylife.pk)

    except Exception:
        print(Exception.message)
    return context


def report_pdf(request):
    template = 'history_report.html'
    media = settings.MEDIA_ROOT
    context = get_context()
    context['media'] = media

    pdf = render_to_pdf(template, context)
    if pdf:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Desposition'] = 'attachment; filename=file.pdf'
        response.write(pdf)
        return response


def report_html(request):
    template = 'history_report.html'
    media = settings.MEDIA_ROOT
    context = get_context()
    context['media'] = media
    return render_to_response(template, context)


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = cStringIO.StringIO()
    pdf = pisa.pisaDocument(cStringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
    if not pdf.err:
        return result.getvalue()
    return False
