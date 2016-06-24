# coding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from mkb.models import ClassMKB


class Hospital(models.Model):
    class Meta:
        db_table = "Hospital"
        verbose_name = "Больница"
        verbose_name_plural = "Больница"

    name_hospit = models.CharField(max_length=100, verbose_name='Имя больницы')
    kodLPO = models.IntegerField(verbose_name='Код ЛПО'),

    def __unicode__(self):
        return self.name_hospit


class Department(models.Model):
    class Meta:
        db_table = "Department"
        verbose_name = "Отделение"
        verbose_name_plural = "Отделение"

    name_dept = models.CharField(max_length=100, verbose_name='Имя отделения')
    hospit_fk = models.ForeignKey(Hospital, related_name='hospital_name', verbose_name='Имя больницы')
    count_ward = models.IntegerField(verbose_name='Общая количество палат')

    def __unicode__(self):
        return self.name_dept


class Post(models.Model):
    class Meta:
        verbose_name_plural = "Должность врача"

    name_post = models.CharField(max_length=100, verbose_name="Должность")

    def __unicode__(self):
        return self.name_post


class Role(models.Model):
    class Meta:
        db_table = "role"
        verbose_name_plural = "Роль"
        verbose_name = "Роль"
    name_role = models.CharField(max_length=100, verbose_name="Роль")

    def __unicode__(self):
        return self.name_role


class StatusGradDegree(models.Model):
    class Meta:
        verbose_name_plural = "Ученная степень"
        verbose_name = "Ученная степень"
    name_pd = models.CharField(max_length=100, verbose_name="Ученная степень")

    def __unicode__(self):
        return self.name_pd


class Doctor(models.Model):
    class Meta:
        verbose_name_plural = "Врач"
        verbose_name = "Врач"
    fio_doc = models.CharField(verbose_name='Ф.И.О', max_length=255)
    date_born_doc = models.DateField(verbose_name='Дата рождения')
    department = models.ForeignKey(Department, verbose_name="Отделение", null=True)
    postDoc = models.ForeignKey(Post, verbose_name="Должность", null=True)
    statusPostDegree = models.ManyToManyField(StatusGradDegree, verbose_name="Ученная степень")
    loginDoc = models.ForeignKey(User, verbose_name="Логин", null=True)
    role_doc = models.ForeignKey(Role, verbose_name="Роль", null=True)
    data_start_career = models.DateField(verbose_name="Дата начало карьеры", null=True)
    address = models.CharField(verbose_name="Адрес", max_length=70, null=True)
    telephone = models.CharField(verbose_name='Телефон', max_length=70, null=True)

    def __unicode__(self):
        return self.fio_doc


class Citizenship(models.Model):
    class Meta:
        db_table = "Citizenship"
        verbose_name = "Гражданство"
        verbose_name_plural = "Гражданство"

    name_citiz = models.CharField(max_length=100, verbose_name='Гражданство')

    def __unicode__(self):
        return self.name_citiz


class Area(models.Model):
    class Meta:
        db_table = "Area"
        verbose_name_plural = "Область"

    name_area = models.CharField(max_length=100, verbose_name='Область')

    def __unicode__(self):
        return self.name_area


class Region(models.Model):
    class Meta:
        db_table = "Region"
        verbose_name = "Район"
        verbose_name_plural = "Район"

    name_reg = models.CharField(max_length=100, verbose_name='Район')
    area_fk = models.ForeignKey(Area, verbose_name='Область')

    def __unicode__(self):
        return self.name_reg


class Town(models.Model):
    class Meta:
        db_table = "Town"
        verbose_name_plural = "Село"
        verbose_name = "Село"

    name_town = models.CharField(max_length=100, verbose_name='Село')
    region_fk = models.ForeignKey(Region, verbose_name='Район')

    def __unicode__(self):
        return self.name_town


class Patient(models.Model):
    class Meta:
        db_table = "Patient"
        verbose_name_plural = "Заись пациента"
        verbose_name = "Заись пациента"

    MALE = 'M'
    FEMALE = 'Ж'
    BLOOD1 = '1'
    BLOOD2 = '2'
    BLOOD3 = '3'
    BLOOD4 = '4'
    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )
    BLOOD_GROUP_CHOICES = (
        (BLOOD1, '1'),
        (BLOOD2, '2'),
        (BLOOD3, '3'),
        (BLOOD4, '4'),
    )
    surname_pat = models.CharField(max_length=100, verbose_name='Фамилия')
    name_pat = models.CharField(max_length=100, verbose_name='Имя')
    last_name_pat = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    date_born_pat = models.DateField(verbose_name='Число, месяц, год рождения')
    rhesusfactor_pat = models.CharField(verbose_name='Резус принадлежность',
                                        max_length=10)
    bloodgroup_pat = models.CharField(choices=BLOOD_GROUP_CHOICES, verbose_name='Группа крови', max_length=10)
    gender_pat = models.CharField(choices=GENDER_CHOICES, verbose_name='Пол', max_length=5)
    citizenship_fk = models.ForeignKey(Citizenship, verbose_name='Гражданство')
    num_social_protec = models.CharField(
        verbose_name='Номер удостоверения социальной защиты', max_length=100)

    category_pat = models.CharField(verbose_name='Категория пациента', max_length=100,
                                    null=True, blank=True)
    retired_pat = models.CharField(verbose_name='Номер удостоверения', max_length=100,
                                   null=True, blank=True)
    place_work_pat = models.CharField(verbose_name='Место работы, должность',
                                      max_length=100, null=True, blank=True)
    area_fk = models.ForeignKey(Area, verbose_name='Область', related_name='area')
    region_fk = models.ForeignKey(Region, verbose_name='Район')
    town_fk = models.ForeignKey(Town, verbose_name='Село')
    street_pat = models.CharField(verbose_name='Улица', max_length=100)
    insurance_territory = models.CharField(max_length=50, verbose_name='Территория страхования', null=True)
    num_medic_record = models.IntegerField(verbose_name='Номер мед. карты')
    login_pat = models.CharField(max_length=100, verbose_name="Логин", null=True, unique=True, blank=True)
    password_pat = models.CharField(max_length=100, verbose_name="Пароль", null=True, blank=True)
    photo_pat = models.ImageField(upload_to='profile/', null=True, verbose_name="Фотография", blank=True)
    email_pat = models.EmailField(verbose_name="Электронный адрес", null=True, unique=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.surname_pat, self.name_pat)


class RecordPatient(models.Model):
    class Meta:
        db_table = "RecordPatient"
        verbose_name_plural = "Результаты анализов"
        verbose_name = "Результаты анализов"

    patient_fk = models.ForeignKey(Patient, verbose_name="Больной")
    hospit_fk = models.ForeignKey(Hospital, verbose_name="Больница")
    dept_fk = models.ForeignKey(Department, related_name='department', verbose_name="Отделение")
    num_ward = models.SmallIntegerField(verbose_name="№ палаты")
    receipt_date = models.DateTimeField(verbose_name="дата поступления", null=True, blank=True)
    issue_date = models.DateTimeField(verbose_name="дата выписки", null=True, blank=True)
    trans_dept_fk = models.ForeignKey(Department, related_name='trans_department',
                                      verbose_name="Переведен в отделение", null=True, blank=True)
    admission_diag = models.ForeignKey(ClassMKB, related_name="admission_diagnose",
                                       verbose_name="Диагноз при поступлении", null=True, blank=True)
    doctor = models.ForeignKey(Doctor, verbose_name="Лечающий врач", null=True, blank=True)

    @property
    def get_full_name(self):
        return "%s %s %s" % (self.patient_fk.surname_pat, self.patient_fk.name_pat, self.patient_fk.last_name_pat)

    def __unicode__(self):
        return "%s %s" % (self.patient_fk.surname_pat, self.patient_fk.name_pat)


# Для инвалидов
class ForDisabled(models.Model):
    class Meta:
        db_table = "ForDisabled"
        verbose_name_plural = "Инвалидность"

    VOV_dsbld = models.BooleanField(verbose_name='ИОВ', )
    desc_dsbld = models.TextField(verbose_name='Описание инвалидности', null=True, blank=True)
    year_dsbld = models.DateField(verbose_name='Год инвалидности', null=True, blank=True)
    group_dsbld = models.SmallIntegerField(verbose_name='Группа инвалидности', null=True, blank=True)
    patient_fk = models.ForeignKey(Patient, verbose_name="Больной")

    def __unicode__(self):
        return self.desc_dsbld


class TypeOperation(models.Model):
    class Meta:
        db_table = "TypeOperation"
        verbose_name = "Хирургические операции"

        verbose_name_plural = "Хирургические операции"

    PROCESS = 'process'
    FINISHED = 'end'
    STATUS_CHOICES = (
        (PROCESS, 'В процессе'),
        (FINISHED, 'Закончен')
    )
    patient_fk = models.ForeignKey(RecordPatient, verbose_name="Больной", null=True)
    doctor_fk = models.ForeignKey(Doctor, verbose_name='Доктор')
    name_tpop = models.CharField(verbose_name='Название операции', max_length=200)
    data_tpop = models.DateTimeField(verbose_name='Дата и время начало операции')
    status_tpop = models.CharField(choices=STATUS_CHOICES, verbose_name='Статус', null=True, blank=True, max_length=50)
    method_anesthesia = models.CharField(verbose_name='метод обезболивания', max_length=150)
    healing_tpop = models.CharField(verbose_name='Осложнения, заживление', max_length=150)
    assistant_doc = models.ManyToManyField(Doctor, related_name="assistantDoc", verbose_name="Ассистенты")

    def __unicode__(self):
        return self.name_tpop


# Проверено
class CheckedAnalyze(models.Model):
    class Meta:
        db_table = "CheckedAnalyze"
        verbose_name = "Проверено"
        verbose_name_plural = "Проверено"

    pediculosis = models.BooleanField(verbose_name='Педикулез')
    scabies = models.BooleanField(verbose_name='Чесотка')
    helminthic_invasion = models.BooleanField(verbose_name='глистной инвазии')
    Wasser_react = models.BooleanField(verbose_name='реация Вассермана')
    flyurografiya = models.BooleanField(verbose_name='Флюорография')
    alcohol = models.BooleanField(verbose_name='Алкоголь')
    botkin = models.BooleanField(verbose_name='Боткин')
    chi = models.BooleanField(verbose_name='ОМС')
    hospit_mode = models.BooleanField(verbose_name='с режимом ознакомлен')
    notified_bodies_MVD = models.BooleanField(verbose_name='Сообщено органам МВД')
    patient_fk = models.ForeignKey(RecordPatient, verbose_name="Больной", null=True)

    def __unicode__(self):
        return self.pediculosis


class CauseIllness(models.Model):
    class Meta:
        db_table = "CauseIllness"
        verbose_name = "Несчастных случаев"
        verbose_name_plural = "Несчастных случаев"

    name_cill = models.CharField(max_length=255,
                                 verbose_name="нечастных случаев")

    def __unicode__(self):
        return self.name_cill


# Кем направлен больной
class Sender(models.Model):
    class Meta:
        db_table = "Sender"

        verbose_name_plural = "Кем был направлен больной"

    name_send = models.CharField(verbose_name='Кем направлен больной',
                                 max_length=255, null=True, blank=True)
    estab_send = models.ForeignKey(Hospital,
                                   verbose_name="наименование лечебного учереждения", null=True, blank=True)
    time_after_ill = models.DateTimeField(
        verbose_name='Госпитализирован в больницу (вне плана) спусия', null=True,
        blank=True)
    cause_illness_fk = models.ManyToManyField(CauseIllness, blank=True, verbose_name="нечастных случаев")

    diag_sender = models.ForeignKey(ClassMKB, verbose_name="Диагноз направившего учреждения", null=True, blank=True)

    patient_fk = models.ForeignKey(RecordPatient, verbose_name="Больной")

    def __unicode__(self):
        return self.name_send


class Diagnosis(models.Model):
    class Meta:
        db_table = "Diagnosis"
        verbose_name = "Установления диагноза"
        verbose_name_plural = "Установления диагноза"

    clinical_diag = models.ForeignKey(ClassMKB, related_name="clinical_diagnose",
                                      verbose_name="Диагноз клинический", null=True, blank=True)
    clinical_diag_time = models.DateTimeField(
        verbose_name='дата установления', null=True,
        blank=True)
    clinical_diag_doctor = models.ForeignKey(Doctor,
                                             verbose_name='Ф.И.О врача', null=True, related_name="clinical_diag_doctor",
                                             blank=True)
    morbus_basalis = models.ForeignKey(ClassMKB, related_name="morbus_basalis",
                                       verbose_name="основная болезнь", null=True, blank=True)
    complicatio_morbus_basalis = models.ForeignKey(ClassMKB,
                                                   related_name="complicto_morbus_basalis",
                                                   verbose_name="осложнение основного заболевания", null=True,
                                                   blank=True)
    morbus_concomitans = models.ForeignKey(ClassMKB,
                                           related_name="morbus_concom",
                                           verbose_name="сопутствующая болезнь", null=True, blank=True)
    final_clinical_diag_time = models.DateTimeField(
        verbose_name='дата установления', null=True,
        blank=True)
    final_clinical_diag_doctor = models.ForeignKey(Doctor,
                                                   verbose_name='Ф.И.О врача', null=True,
                                                   related_name="final_clin_diag_doctor",
                                                   blank=True)
    patient_fk = models.ForeignKey(RecordPatient, verbose_name="Больной")

    def __unicode__(self):
        return self.clinical_diag.name


class Drug(models.Model):
    class Meta:
        db_table = "drug"
        verbose_name = "Лекарство"
        verbose_name_plural = "Лекарство"

    name_drug = models.CharField(max_length=100, verbose_name="Лекарство")

    def __unicode__(self):
        return self.name_drug


class EffectsDrugs(models.Model):
    class Meta:
        db_table = "EffectsDrugs"
        verbose_name = "Побочные действия лекарств"
        verbose_name_plural = "Побочные действия лекарств"

    drug = models.ForeignKey(Drug, verbose_name="Лекарство")
    descriptionDrugs = models.CharField(max_length=255, verbose_name="Описание побочное")
    patient = models.ForeignKey(RecordPatient, verbose_name="Больной")

    def __unicode__(self):
        return self.drug.name_drug
