# coding: utf-8
from random import randint

from django.contrib import admin
from nested_admin.nested import NestedModelAdmin, NestedStackedInline
from slugify import slugify

from Analyze.models import BloodChemistry, UrineAnalysis, PTIAnalysis, GenBloodAnalyse
from KIF.models import Hospital, Department, Patient, Region, Area, CheckedAnalyze, TypeOperation, Citizenship, Town, \
    Sender, CauseIllness, RecordPatient, Diagnosis, ForDisabled, EffectsDrugs, Drug, Doctor


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


class TypeOperationInline(NestedStackedInline):
    model = TypeOperation
    extra = 0


class DiagnosisInline(NestedStackedInline):
    model = Diagnosis
    extra = 0
    exclude = ('clinical_diag_doctor', 'final_clinical_diag_doctor')


class ForDisabledInline(NestedStackedInline):
    model = ForDisabled
    extra = 0


class EffectDrugsInline(NestedStackedInline):
    model = EffectsDrugs
    extra = 0


class SenderInline(NestedStackedInline):
    model = Sender
    extra = 0


class RecordPatientInline(NestedStackedInline):
    model = RecordPatient
    extra = 0
    inlines = [
        DiagnosisInline, TypeOperationInline, EffectDrugsInline, SenderInline
    ]
    readonly_fields = ('doctor',)


class PatientAdmin(NestedModelAdmin):
    inlines = [
        RecordPatientInline, ForDisabledInline
    ]

    def save_model(self, request, obj, form, change):
        surname_pat = slugify(obj.surname_pat)
        name_pat = slugify(obj.name_pat)[:1]
        if not obj.login_pat:
            create_login = (str(surname_pat) + str(name_pat) + str(random_with_N_digits(4))).lower()
            obj.login_pat = create_login
        if not obj.password_pat:
            obj.password_pat = (str(surname_pat[:1]) + str(name_pat) + str(obj.date_born_pat).replace('-', '')).lower()
        obj.save()

    readonly_fields = ('login_pat', 'password_pat',)

    def save_formset(self, request, form, formset, change):

        instances = formset.save(commit=False)

        for instance in instances:
            if not isinstance(instance, RecordPatient):
                if not instance.final_clinical_diag_doctor:
                    instance.final_clinical_diag_doctor = Doctor.objects.get(loginDoc=request.user)
                if not instance.clinical_diag_doctor:
                    instance.clinical_diag_doctor = Doctor.objects.get(loginDoc=request.user)
            else:
                instance.doctor = Doctor.objects.get(loginDoc=request.user)

            instance.save()
        formset.save_m2m()


class GenBloodAnalyseInline(NestedStackedInline):
    model = GenBloodAnalyse
    extra = 0
    readonly_fields = GenBloodAnalyse._meta.get_all_field_names()


class BloodChemistryInline(NestedStackedInline):
    model = BloodChemistry
    extra = 0
    readonly_fields = BloodChemistry._meta.get_all_field_names()


class UrineAnalysisInline(NestedStackedInline):
    model = UrineAnalysis
    extra = 0
    readonly_fields = UrineAnalysis._meta.get_all_field_names()


class PTIAnalysisInline(NestedStackedInline):
    model = PTIAnalysis
    extra = 0
    readonly_fields = PTIAnalysis._meta.get_all_field_names()


class AnalyzeAdmin(NestedModelAdmin):
    inlines = [GenBloodAnalyseInline, BloodChemistryInline, UrineAnalysisInline, PTIAnalysisInline]
    readonly_fields = ('patient_fk', 'hospit_fk', 'dept_fk', 'num_ward', 'receipt_date', 'issue_date', 'trans_dept_fk',
                       'admission_diag', 'doctor')


admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Region)
admin.site.register(Area)
admin.site.register(CheckedAnalyze)
admin.site.register(TypeOperation)
admin.site.register(Citizenship)
admin.site.register(Town)
admin.site.register(CauseIllness)
admin.site.register(Sender)
admin.site.register(Diagnosis)
admin.site.register(RecordPatient, AnalyzeAdmin)
admin.site.register(ForDisabled)
admin.site.register(EffectsDrugs)
admin.site.register(Drug)
