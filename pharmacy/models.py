# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from KIF.models import RecordPatient, Drug, Doctor


class StockTacking(models.Model):
    class Meta:
        db_table = "stocktacking"
        verbose_name_plural = "Учет лекарств"

    drugSt = models.ForeignKey(Drug, verbose_name="Лекарство")
    date = models.DateTimeField(verbose_name="Дата")
    amount = models.IntegerField(verbose_name="Количество лекарств")
    rest = models.IntegerField(verbose_name="Манупуляция количеством")
    doctor = models.ForeignKey(Doctor, verbose_name="Аптекарь", null=True)

    def __unicode__(self):
        return self.drugSt.name_drug


class AppointmentList(models.Model):
    class Meta:
        db_table = "appointmentlist"

        verbose_name_plural = "Лист назначения"

    patient = models.ForeignKey(RecordPatient, verbose_name="Пациент", null=True)
    drugAl = models.ForeignKey(Drug, verbose_name="Лекарство")
    descriptionDrinkDrug = models.TextField(verbose_name="Описание", null=True, blank=True)
    beginAppointment = models.DateTimeField(verbose_name="Дата назначения")
    endAppointment = models.DateTimeField(verbose_name="Дата отмены", null=True, blank=True)
    sourceDrug = models.CharField(verbose_name="Источник получения лекарств", max_length=30, null=True, blank=True)
    amount = models.IntegerField(verbose_name="Количество препаратов")
    doctor = models.ForeignKey(Doctor, verbose_name="Доктор", null=True)

    def __unicode__(self):
        return self.drugAl.name_drug


class AcceptanceList(models.Model):
    class Meta:
        db_table = "acceptancelist"

        verbose_name_plural = "Время принятия лекарств"

    appointmentList = models.ForeignKey(AppointmentList)
    acceptDate = models.DateTimeField(verbose_name="Времчя принятия лекарств")
    amount = models.IntegerField(verbose_name="Количество выпивших препаратов")
