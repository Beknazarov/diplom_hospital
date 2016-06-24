# coding: utf-8
from django.contrib.admin import AdminSite
from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from Analyze.models import BloodChemistry, UrineAnalysis, PTIAnalysis, Color, GenBloodAnalyse
from KIF.models import RecordPatient, Doctor


class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'


admin_analyze = MyAdminSite(name='myadmin')


class GenBloodAnalyseInline(NestedStackedInline):
    model = GenBloodAnalyse
    extra = 0
    exclude = ('doctor',)


class BloodChemistryInline(NestedStackedInline):
    model = BloodChemistry
    extra = 0
    exclude = ('doctor',)


class UrineAnalysisInline(NestedStackedInline):
    model = UrineAnalysis
    extra = 0
    exclude = ('doctor',)


class PTIAnalysisInline(NestedStackedInline):
    model = PTIAnalysis
    extra = 0
    exclude = ('doctor',)


class AnalyzeAdmin(NestedModelAdmin):
    inlines = [GenBloodAnalyseInline, BloodChemistryInline, UrineAnalysisInline, PTIAnalysisInline]
    readonly_fields = (
        'patient_fk', 'hospit_fk', 'dept_fk', 'num_ward', 'receipt_date', 'issue_date', 'trans_dept_fk',
        'admission_diag', 'doctor')

    def save_formset(self, request, form, formset, change):

        instances = formset.save(commit=False)

        for instance in instances:
            if not instance.doctor:
                instance.doctor = Doctor.objects.get(loginDoc=request.user)
            instance.save()
        formset.save_m2m()


# class GenBloodAnalyzeAdmin(NestedModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not obj.doctor:
#             obj.doctor = Doctor.objects.get(loginDoc=request.user)
#         obj.save()


admin_analyze.register(RecordPatient, AnalyzeAdmin)
admin_analyze.register(GenBloodAnalyse)
admin_analyze.register(BloodChemistry)
admin_analyze.register(UrineAnalysis)
admin_analyze.register(PTIAnalysis)
admin_analyze.register(Color)
