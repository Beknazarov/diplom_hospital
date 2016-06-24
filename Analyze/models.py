# coding: utf-8
from __future__ import unicode_literals

import hashlib

from django.db import models

from KIF.models import RecordPatient, Department, Doctor


class PatientInfo(models.Model):
    patient = models.ForeignKey(RecordPatient, verbose_name="Пациент")
    doctor = models.ForeignKey(Doctor, verbose_name="Доктор", null=True, blank=True)
    compl_date = models.DateTimeField(verbose_name="дата сдачи")

    class Meta:
        abstract = True



# Биохимический анализ крови
class BloodChemistry(PatientInfo):
    class Meta:
        db_table = "BloodChemistry"
        verbose_name_plural = "Биохимический анализ крови"
        verbose_name = "Биохимический анализ крови"

    department = models.ForeignKey(Department, verbose_name="Отделение")
    total_protein = models.FloatField(verbose_name="Общий белок")
    albumin = models.FloatField(verbose_name="Альбумины")
    globulins = models.FloatField(verbose_name="глобулины")
    alpha1 = models.FloatField(verbose_name="альфа-1")
    alpha2 = models.FloatField(verbose_name="альфа-2")
    betta = models.FloatField(verbose_name="бетта")
    gamma = models.FloatField(verbose_name="гамма")
    RAGform = models.FloatField(verbose_name="К=А/Г")
    urea = models.FloatField(verbose_name="мочевина")
    creatinine = models.FloatField(verbose_name="креатинин")
    resudual_nitrogen = models.FloatField(verbose_name="остаточный азот", null=True, blank=True)
    thymol_test = models.FloatField(verbose_name="тимоловая проба")
    sulemovaya_test = models.FloatField(verbose_name="сулемовая проба")
    T_ara_test = models.FloatField(verbose_name="Проба Т-Ара")
    total_bilirubin = models.FloatField(verbose_name="Билирубин общий")
    straight_bilirubin = models.FloatField(verbose_name="Билирубин прямой")
    indirect_bilirubin = models.FloatField(verbose_name="Билирубин непрямой", null=True, blank=True)
    alt = models.FloatField(verbose_name="АЛТ")
    ast = models.FloatField(verbose_name="АСТ")
    alpha_amylase = models.FloatField(verbose_name="Альфа-амилаза")
    creatine_phosphokinase = models.FloatField(verbose_name="Креатинфосфокиназа")
    holinestereza = models.FloatField(verbose_name="Холинэстераза")
    acidic_phosphatase = models.FloatField(verbose_name="фосфатаза кислая")
    alkaline_phosphatase = models.FloatField(verbose_name="фосфатаза щелочная")
    LAP = models.FloatField(verbose_name="Л А П")
    cholesterol = models.FloatField(verbose_name="Холестерин")
    general_lipydy = models.FloatField(verbose_name="Общие липйды")
    beta_lipoproteins = models.FloatField(verbose_name="Бетта липопротеиды")
    triglycerides = models.FloatField(verbose_name="Трилглицериды")
    haptoglobin = models.FloatField(verbose_name="Гаптоглобин")
    hepatocuprein = models.FloatField(verbose_name="Церулоплазмин")
    sialic_test = models.FloatField(verbose_name="Сиаловая проба")
    C_reactive_protein = models.FloatField(verbose_name="'С' реактивный белок")
    zhokinena_reaction = models.FloatField(verbose_name="Реакция Жокинена")
    potassium = models.FloatField(verbose_name="Калий")
    sodium = models.FloatField(verbose_name="Натрий")
    chlorides = models.FloatField(verbose_name="Хлориды")
    calcium = models.FloatField(verbose_name="Кальций")
    phosphorus = models.FloatField(verbose_name="Фосфор")
    iron = models.FloatField(verbose_name="Железо")
    blood_glucose = models.FloatField(verbose_name="Глюкоза крови")
    glucose_urine = models.FloatField(verbose_name="Глюкоза в моче")
    pyruvic_k_ta = models.FloatField(verbose_name="Пировиноградная к-та")
    uric_acid = models.FloatField(verbose_name="Мочевая кислота")
    CS17 = models.FloatField(verbose_name="17 КС")




# Общий анализ крови
class GenBloodAnalyse(PatientInfo):
    class Meta:
        db_table = "GenBloodAnalyse"
        verbose_name_plural = "Общий анализ крови"
        verbose_name = "Общий анализ крови"

    gen_analys_number = models.IntegerField(verbose_name="№")
    erythrocytes = models.FloatField(verbose_name="Эритроциты", help_text="10 12/ л")
    hemoglobin = models.FloatField(verbose_name="Гемоглобин", help_text="80-100 г/л")
    color_index = models.FloatField(verbose_name="Цветной показатель", help_text="0.8-1.0")
    polychrome = models.FloatField(verbose_name="Полихром", help_text="+")
    basophil = models.FloatField(verbose_name="базоф.", help_text="-")
    reticulocytes = models.FloatField(verbose_name="Ретикулоциты", help_text="0.6-0.8")
    platelets = models.FloatField(verbose_name="Тромбоциты", help_text="250-400 тысяч")
    vermin = models.FloatField(verbose_name="Паразиты")
    leukocytes = models.FloatField(verbose_name="Лейкоциты", help_text="Норма 6-8 тысяч 10/9л")
    basophils = models.FloatField(verbose_name="Базофилы", help_text="30-40")
    eozofily = models.FloatField(verbose_name="Эозинофилы", help_text="180-200")
    mielots = models.FloatField(verbose_name="Миэлоц", help_text="-")
    young = models.FloatField(verbose_name="Юные", help_text="-")
    paloch = models.FloatField(verbose_name="Палоч", help_text="-")
    segment = models.FloatField(verbose_name="Сегмент", help_text="4020-5040")
    lymphocytes = models.FloatField(verbose_name="Лимфоциты", help_text="1800-240С")
    monocytes = models.FloatField(verbose_name="Моноциты", help_text="360-640")
    shear_index = models.FloatField(verbose_name="Индекс сдвига", help_text="0-6")
    anisocytosis = models.FloatField(verbose_name="Анизоцитоз")
    eryth_resistance = models.FloatField(verbose_name="резистентность эритроцитов?????")
    microplania = models.FloatField(verbose_name="пойкилоцитоз")
    convolution_blood = models.FloatField(verbose_name="Свертыв, крови")
    normoblasts = models.FloatField(verbose_name="Нормобласты")
    normob_start = models.FloatField(verbose_name="Начало")
    eryth_sediment = models.FloatField(verbose_name="оседание эритроцитов (СОЭ)")
    eryth_sediment_end = models.FloatField(verbose_name="конец")


class PTIAnalysis(PatientInfo):
    class Meta:
        db_table = "PTIAnalysis"
        verbose_name_plural = "Протромбированный индекс"
        verbose_name = "Протромбированный индекс"

    PTI = models.FloatField(verbose_name="ПТИ")
    SSK = models.FloatField(verbose_name="ССК")


class Color(models.Model):
    class Meta:
        db_table = "Color"
        verbose_name_plural = "Цвет"
        verbose_name = "Цвет"
    name_color = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name_color


class UrineAnalysis(PatientInfo):
    class Meta:
        db_table = "UrineAnalysis"
        verbose_name_plural = "Анализ мочи"
        verbose_name = "Анализ мочи"
    count_urin = models.FloatField(verbose_name="Количество")
    count_urin_liter = models.FloatField(verbose_name="л*)")
    count_urin_milliliter = models.FloatField(verbose_name="мл**)")
    color_fk = models.ForeignKey(Color, verbose_name="Цвет")
    transparency = models.FloatField(verbose_name="прозрачность???")
    relative_density = models.FloatField(verbose_name="относительная плотность")
    reaction = models.FloatField(verbose_name="реакция")
    protein = models.FloatField(verbose_name="белок")
    protein_mmol = models.FloatField(verbose_name="г/л*")
    protein_g = models.FloatField(verbose_name="г%**")
    ketone_body = models.FloatField(verbose_name="кетоновые тела????")
    reaction_blood = models.FloatField(verbose_name="реакция на кровь???")
    bilirubin = models.FloatField(verbose_name="билирубин")
    urobilinoidy = models.FloatField(verbose_name="уробилиноиды")
    bile_acid = models.FloatField(verbose_name="желчные кислоты")
    Indican = models.FloatField(verbose_name="индикан")
    unit_replaced = models.FloatField(verbose_name="единицы подлежащие замене")
    epithelium_flat = models.FloatField(verbose_name="эпителий")
    epithelium_transition = models.FloatField(verbose_name="плоский")
    epithelium_renal = models.FloatField(verbose_name="переходный")
    leukocytes = models.FloatField(verbose_name="лейкоциты")
    erythrocytes_invariable = models.FloatField(verbose_name="эритроциты неизмененное")
    erythrocytes_amend = models.FloatField(verbose_name="эритроциты измененные")
    cylinders_hyaline = models.FloatField(verbose_name="цилиндры гиалиновые")
    cylinders_grained = models.FloatField(verbose_name="зернистые")
    cylinders_waxy = models.FloatField(verbose_name="восковидные")
    cylinders_epithelial = models.FloatField(verbose_name="эпителиальные")
    cylinders_leukocyte = models.FloatField(verbose_name="лейкоцитарные")
    cylinders_erythrocyte = models.FloatField(verbose_name="эритроцитарные")
    cylinders_pigment = models.FloatField(verbose_name="пигментные")
    slime = models.FloatField(verbose_name="слизь")
    salt = models.FloatField(verbose_name="соли")
    bacteria = models.FloatField(verbose_name="бактерии???")

    def __unicode__(self):
        return self.color_fk.name_color
