from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from Analyze.models import GenBloodAnalyse, BloodChemistry, PTIAnalysis
from KIF.models import RecordPatient


class GenerateAnalyze(ListView):
    model = GenBloodAnalyse
    template_name = "analyze.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('patient'):
            return HttpResponseRedirect(reverse('login'))
        else:
            return super(GenerateAnalyze, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GenerateAnalyze, self).get_context_data(**kwargs)
        patient_session_id = self.request.session.get('patient')
        profile = RecordPatient.objects.filter(patient_fk=patient_session_id)
        context['profile_view'] = profile
        context['gen_analyze_blood_view'] = GenBloodAnalyse.objects.filter(patient=patient_session_id)
        context['blood_chemistry_analyze_view'] = BloodChemistry.objects.filter(patient=patient_session_id)
        context['pti_analyze_view'] = PTIAnalysis.objects.filter(patient=patient_session_id)
        return context
