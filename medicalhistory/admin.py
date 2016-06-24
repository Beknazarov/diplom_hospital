# -*- coding:utf-8 -*-
from django.contrib import admin
from  django.db import models
from django_select2 import forms as select_form
from easy_select2 import select2_modelform
from nested_admin.nested import forms
from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from .models import *

# admin.site.register(PatientConditionsNow)

# справочники

admin.site.register(Infection)
admin.site.register(Disease)


class StatusLocalisAdmin(admin.StackedInline):
    model = StatusLocalis
    extra = 0


class NeuroPsychologicalSystemAdmin(admin.StackedInline):
    model = NeuroPsychologicalSystem
    extra = 0


class GenitoUrinarySystemAdmin(admin.StackedInline):
    model = GenitoUrinarySystem
    extra = 0


class EndocrineSystemAdmin(admin.StackedInline):
    model = EndocrineSystem
    extra = 0


class DigestiveSystemAdmin(admin.StackedInline):
    model = DigestiveSystem
    extra = 0


class CardiovascularSystemAdmin(admin.StackedInline):
    model = CardiovascularSystem
    extra = 0

class SensesAdmin(admin.StackedInline):
    model = Senses
    extra = 0

class RespiratorySystemAdmin(admin.StackedInline):
    model = RespiratorySystem
    extra = 0


class WomanAdmin(admin.StackedInline):
    model = Women
    extra = 0


class PatientConditionsNowAdmin(admin.StackedInline):
    model = PatientConditionsNow
    extra = 0
    # fieldsets = (
    #     ('----', {
    #         'classes': ('collapse',),
    #         'fields': ('general_state', 'weight', 'height', 'body')
    #     }),
        # ('Положение', {
        #     'classes': ('collapse',),
        #     'fields': ('position', 'skin', 'subcutaneous_tissue',
        #                'nails', 'muscles', 'bones',
        #                'joints', 'lymph_node')
        #}
    #)
    #)



# HistoryForm = select2_modelform(HistoryPatientLife, attrs={'width': '500px'})

class HistoryPatientLifeAdmin(admin.ModelAdmin):
    # form = HistoryForm
    # fields = ('social_conditions',
    #           'harmful_profession',
    #           'retired',
    #           'disability_group',
    #            'disability_years',
    #           'smoking_year',
    #             'smoking_packs_day',
    #           'alcohol_years',
    #           'disease',
    #           'infection',
    #           'allergic_history',
    #           'risk_factors',
    #           'recordpatient')
    inlines = [
        PatientConditionsNowAdmin,
        WomanAdmin,
        SensesAdmin,
        RespiratorySystemAdmin,
        CardiovascularSystemAdmin,
        DigestiveSystemAdmin,
        GenitoUrinarySystemAdmin,
        EndocrineSystemAdmin,
        NeuroPsychologicalSystemAdmin,
        StatusLocalisAdmin,
    ]


admin.site.register(HistoryPatientLife, HistoryPatientLifeAdmin)
# admin.site.register(HistoryPatientLife)