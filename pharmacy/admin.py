# coding: utf-8
from django.contrib import admin

from pharmacy.models import StockTacking, AppointmentList, AcceptanceList


class ModelAppointmentListAdmin(admin.ModelAdmin):
    list_display = ('drugAl', 'patient', 'beginAppointment', 'amount')
    search_fields = ('drugAl__name_drug', 'patient__patient_fk__name_pat', 'patient__patient_fk__surname_pat',
                     'patient__patient_fk__last_name_pat')
    readonly_fields = (
        'drugAl', 'patient', 'beginAppointment', 'endAppointment', 'amount', 'doctor', 'sourceDrug',
        'descriptionDrinkDrug')


class ModelStockTackingAdmin(admin.ModelAdmin):
    list_display = ('drugSt', 'date', 'amount', 'rest')

    readonly_fields = ('drugSt', 'date', 'amount', 'rest', 'doctor')


class ModelAcceptanceListAdmin(admin.ModelAdmin):
    list_display = ('appointmentList', 'acceptDate', 'amount')

    readonly_fields = ('appointmentList', 'acceptDate', 'amount')


admin.site.register(StockTacking, ModelStockTackingAdmin)
admin.site.register(AppointmentList, ModelAppointmentListAdmin)
admin.site.register(AcceptanceList, ModelAcceptanceListAdmin)
