# coding=utf-8
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from mkb.models import ClassMKB

from KIF.models import RecordPatient



class HistoryPatientLife(models.Model):
    SOCIAL_COND = (
        ('удовлетворительные', 'удовлетворительные'),
        ('неудовлетворительные', 'неудовлетворительные'),
        ('хорошие', 'хорошие'),
    )
    DISABILITY_GROUPS = (
        (1, 'Первая группа'),
        (2, 'Вторая группа'),
        (3, 'Третья группа'),
    )
    social_conditions = models.CharField(max_length=150, verbose_name='Социально бытовые условия', choices=SOCIAL_COND)
    harmful_profession = models.CharField(max_length=300,
                                          verbose_name='Профвредности')
    retired = models.PositiveSmallIntegerField(verbose_name='На пенсии (возраст)',
                                          validators=[MaxValueValidator(150)],
                                          blank=True,
                                          null=True)
    disability_group = models.PositiveSmallIntegerField(verbose_name='Группа инвалидности',
                                                   choices=DISABILITY_GROUPS,
                                                   blank=True,
                                                   validators=[MaxValueValidator(3)], )
    disability_years = models.DateField(verbose_name='Инвалидность с года',
                                        blank=True,
                                        null=True)  # ? узнать дата как хранить только год
    smoking_year = models.PositiveSmallIntegerField(verbose_name='Курение (с лет)',
                                                    validators=[MaxValueValidator(150), MinValueValidator(4)],
                                                    null=True,
                                                    blank=True)
    smoking_packs_day = models.PositiveSmallIntegerField(verbose_name='Курение пачек в день',
                                                         validators=[MaxValueValidator(10)],
                                                         null=True,
                                                         blank=True)
    alcohol_years = models.PositiveSmallIntegerField(verbose_name='Употребление алкоголя(возраст)',
                                                     blank=True,
                                                     validators=[MaxValueValidator(150)],
                                                     null=True)
    disease = models.ManyToManyField('Disease',
                                     verbose_name='Травмы и болезни',
                                     blank=True, related_name="diseases")

    infection = models.ManyToManyField('Infection', verbose_name='Инфекционные заболевания',
                                       blank=True, related_name="infections")
    allergic_history = models.TextField(verbose_name='Аллергологический анемез')
    risk_factors = models.TextField(verbose_name='Факторы риска')
    recordpatient = models.OneToOneField(RecordPatient, verbose_name='Пациент')  # временный пациент

    class Meta:
        db_table = 'history_patient_life'
        verbose_name = 'История жизни пациента'
        verbose_name_plural = 'Истории жизни пациента'
    def __unicode__(self):
        return self.recordpatient.patient_fk.surname_pat

class Disease(models.Model):
    disease = models.TextField(verbose_name="Название травмы")

    class Meta:
        db_table = 'disease'
        verbose_name = 'Травма'
        verbose_name_plural = 'Травмы'

    def __unicode__(self):
        return self.disease


class Infection(models.Model):
    infection = models.TextField(verbose_name="Инфекции")

    class Meta:
        db_table = 'infection'
        verbose_name = 'Инфекционное заболевание'
        verbose_name_plural = 'Инфекционные заболевания'

    def __unicode__(self):
        return self.infection


# у женщин
class Women(models.Model):
    MENSTRUATION_ACHES = (
        ('болезненно', 'болезненно'),
        ('неболезненно', 'неболезненно'),
    )
    MENSTRUATION_REGULAR = (
        ('регулярные', 'регулярные'),
        ('нерегулярные', 'нерегулярные'),
    )
    menstruation_ache = models.CharField(max_length=50, verbose_name=("Месячные(болезненность)"),
                                         choices=MENSTRUATION_ACHES,
                                         blank=True,
                                         null=True)
    mensrtuation_regularity = models.CharField(max_length=50,
                                               verbose_name='Месячные(регулярность)',
                                               choices=MENSTRUATION_REGULAR,
                                               blank=True,
                                               null=True, )
    menstruation_years = models.PositiveSmallIntegerField(verbose_name='Месячные(с лет)',
                                                          validators=[MaxValueValidator(150)],
                                                          blank=True,
                                                          null=True)
    climax_years = models.PositiveSmallIntegerField(verbose_name='Климакс(с лет)',
                                                    validators=[MaxValueValidator(150)],
                                                    blank=True,
                                                    null=True)
    pregnancy_count = models.PositiveSmallIntegerField(verbose_name='Число беременностей',
                                                       validators=[MaxValueValidator(50)],
                                                       default=0)
    childbirth_count = models.PositiveSmallIntegerField(verbose_name='Число родов',
                                                        validators=[MaxValueValidator(50)],
                                                        default=0)
    miscarriages_count = models.PositiveSmallIntegerField(verbose_name='Число выкидышей',
                                                          validators=[MaxValueValidator(50)],
                                                          default=0)
    pregnancy_proceeds = models.TextField(verbose_name='Течение беременности', blank=True, null=True)
    mammary_gland = models.TextField(verbose_name='Молочные железы', blank=True, null=True)
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'women'
        verbose_name = 'У женщин'
        verbose_name_plural = 'У женщин'


# состояние пациента в данное время
class PatientConditionsNow(models.Model):
    BODY_TYPES = (
        ('астеническое', 'астеническое'),
        ('нормостеническое', 'нормостеническое'),
        ('гиперстеническое', 'гиперстеническое'),
    )
    POSITION_TYPES = (
        ('активное', 'активное'),
        ('вынужденное', 'вынужденное'),
    )
    general_state = models.TextField(verbose_name='Общее состояние', blank=True)
    weight = models.FloatField(verbose_name='Вес(кг.)',
                               validators=[MaxValueValidator(1000)],
                               blank=True)
    height = models.FloatField(verbose_name='Рост(м.)',
                               validators=[MaxValueValidator(5)],
                               blank=True)
    body = models.CharField(max_length=100,
                            verbose_name='Телосложение',
                            choices=BODY_TYPES,
                            blank=True)

    position = models.CharField(max_length=150,
                                verbose_name='Положение',
                                choices=POSITION_TYPES,
                                blank=True)

    skin = models.CharField(max_length=150, verbose_name='Кожные покровы', blank=True)

    subcutaneous_tissue = models.CharField(max_length=150, verbose_name='Подкожная клетчатка', blank=True)
    nails = models.CharField(max_length=150, verbose_name='Ногти', blank=True)

    muscles = models.CharField(max_length=100, verbose_name='Мышцы', blank=True)

    bones = models.CharField(max_length=100, verbose_name='Кости', blank=True)

    joints = models.CharField(max_length=100, verbose_name='Суставы', blank=True)

    lymph_node = models.CharField(max_length=150, verbose_name='Лимфатические узлы', blank=True)
    history = models.OneToOneField(HistoryPatientLife, related_name='history')

    class Meta:
        db_table = 'patient_conditions_now'
        verbose_name = 'Состояние больного в данный момент'
        verbose_name_plural = 'Состояние больного в данный момент'


class Senses(models.Model):
    senses_cond = models.CharField(max_length=150, verbose_name='Органы чусвтв(общее состояние)', blank=True)
    eyes = models.CharField(max_length=150, verbose_name='Глаза', blank=True)
    hearing = models.CharField(max_length=150, verbose_name='Слух', blank=True)
    skin_sensitivity = models.CharField(max_length=150, verbose_name='Чувствительность  кожных покровов', blank=True)
    smell = models.CharField(max_length=150, verbose_name='Обоняние', blank=True)
    history = models.OneToOneField(HistoryPatientLife)

    class Meta:
        db_table = 'senses'
        verbose_name = 'Органы чувств больного'
        verbose_name_plural = 'Органы чувств больного'


# Система дыхания(sistema respiratorius)
class RespiratorySystem(models.Model):
    PARTICIPATION_CHEST_TYPES = (
        ('симметрично', 'симметрично'),
        ('отстает справа', 'отстает справа'),
        ('отстает слева', 'отстает слева'),)
    VOICE_TREMORS = (
        ('одинаковое с обеих сторон', 'одинаковое с обеих сторон'),
        ('усилено', 'усилено'),
        ('ослаблено', 'ослаблено'),)
    OMISSION_LOWER_BOUND = (
        ('границы в норме', 'одинаковое с обеих сторон'),
        ('опущено на одно ребро', 'опущено на одно ребро'),
        ('опущено на два ребра', 'опущено на два ребра'),
    )
    PERCUSSION = (
        ('легочный звук(нормальный)', 'легочный звук(нормальный)'),
        ('коробочный', 'коробочный'),
        ('притупленный справа', 'притупленный справа'),
        ('притупленный слева', 'притупленный слева'),
    )
    MOBILITY=(
        ('в норме', 'в норме'),
        ('на одно ребро', 'на одно ребро'),
        ('на два ребра', 'на одно ребро'),
        ('на три ребра', 'на одно ребро'),
    )
    nasal_breathing = models.CharField(max_length=120, blank=True, verbose_name='Носовое дыхание')
    rib_cage = models.CharField(max_length=150, verbose_name='Грудная клетка')
    part_chest_breathing = models.CharField(max_length=40,
                                            blank=True,
                                            verbose_name='Участие грудной клетки в акте дыхания',
                                            choices=PARTICIPATION_CHEST_TYPES)
    part_breathing_muscle = models.CharField(max_length=150,
                                             verbose_name='Участие в акте дыхания мышц')
    voice_tremor = models.CharField(max_length=150, verbose_name='Голосовое дрожание', choices=VOICE_TREMORS)
    percussion_lung = models.CharField(max_length=150, choices=PERCUSSION,verbose_name='Перкуссия легких')
    omision_lower_bound = models.CharField(max_length=150,
                                           verbose_name='Опущение нижних границ',
                                           choices=OMISSION_LOWER_BOUND)
    mobility_bottom_lungs = models.CharField(max_length=150, verbose_name='Подвижность нижнего края легких',choices=MOBILITY)
    auscultation_lungs = models.CharField(max_length=150, verbose_name='Аускультация легких:дыхание')
    wheezing = models.CharField(max_length=150, verbose_name='Хрипы')
    count_breaths_perminute = models.PositiveSmallIntegerField(verbose_name='Число дыханий в минуту',
                                                               null=True, blank=True,
                                                               validators=[MaxValueValidator(200)])
    breathing_rhythm = models.CharField(max_length=150, verbose_name='Ритм дыхания')
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'respiratory_system'
        verbose_name = 'Система дыхания'
        verbose_name_plural = 'Система дыхания'


# Сердечно сосудистая система(Sistema cardiovasularis)
class CardiovascularSystem(models.Model):
    AUSCULATIONS_HEART = (
        ('II тон сохранен', 'II тон сохранен'),
        ('ослаблен', 'ослаблен'),
        ('акцент', 'акцент'),
    )

    AUSCULATIONS_HEART_FLAP = (
        ('шумов нет', 'шумов нет'),
        ('слабо выражена', 'слабо выражена'),
        ('сильно выражена', 'слабо выражена'),
    )

    ARTERIES = (
        ('пульсация сохранене в норме', 'пульсация сохранене в норме'),
        ('симметрично', 'симметрично'),
        ('ослаблена', 'ослаблена'),
    )
    NOICE_AROUND = AUSCULATIONS_HEART_FLAP
    when_viewed = models.CharField(max_length=150, verbose_name='При осмотре')
    epigastric_pulsation = models.CharField(max_length=150, verbose_name='Эпигастральная пальпация')
    visible_heart_pulsation = models.CharField(max_length=150, verbose_name='Видимые на глаз сердечные пульсации')
    cyanosis = models.CharField(max_length=150, verbose_name='Цианоз')
    apical_impulse = models.CharField(max_length=150, verbose_name='Верхушечный толчок')
    # between_ribs = models.PositiveSmallIntegerField(verbose_name='Межребрие',null=True,blank=True,validators=[MaxValueValidator(7)])
    left_bound_heart = models.CharField(max_length=150, verbose_name='Левая граница сердца')
    right_bound_heart = models.CharField(max_length=150, verbose_name='Правая граница сердца')
    top_bound_heart = models.CharField(max_length=150, verbose_name='Верхняя граница сердца')
    vacular_bundle = models.CharField(max_length=150, verbose_name='Сосудистый пучок')
    ausculation_heart_top = models.CharField(max_length=150, verbose_name='Аускультация сердца: на верхушке',
                                             choices=AUSCULATIONS_HEART)
    systolic_murmur = models.CharField(max_length=150, verbose_name='Систолический шум', null=True)
    diastolic_murmur = models.CharField(max_length=150, verbose_name='Диастолический шум', null=True)
    aorta = models.CharField(max_length=150, verbose_name='Аускультация сердца:на аорте', choices=AUSCULATIONS_HEART)
    systolic_diastolic_noise = models.CharField(max_length=150, verbose_name='Систолический и диастолический шумы',
                                                null=True)
    in_pulmonary_artery = models.CharField(max_length=150, verbose_name='Аускультация сердца:на легочной артерии',
                                           choices=AUSCULATIONS_HEART)
    systolic_diastolic_noise_2 = models.CharField(max_length=150, verbose_name='Систолический и диастолический шумы',
                                                  null=True)
    flap_3_valve = models.CharField(max_length=150, verbose_name='Аускультация сердца:на 3-х створчатом клапане',
                                    choices=AUSCULATIONS_HEART_FLAP)
    left_ebge_sternum = models.CharField(max_length=150, verbose_name='Аускультация сердца:По левому краю грудины',
                                         choices=AUSCULATIONS_HEART)
    arteries = models.CharField(max_length=150, verbose_name='Артерии', choices=ARTERIES)
    vien = models.CharField(max_length=150, verbose_name='Вены')
    pulse_rhythm = models.CharField(max_length=150, verbose_name='Пульс-Ритм')
    pulse_frequency = models.PositiveSmallIntegerField(verbose_name='Пульс-Частота',
                                                       validators=[MaxValueValidator(100)])
    pulse_deficit = models.CharField(max_length=150, verbose_name='Дефицит пульса')
    blood_pressure_top = models.PositiveSmallIntegerField(validators=[MaxValueValidator(180)],
                                                          verbose_name='Артериальное давление(верхнее, мм.рт.ст.)')
    blood_pressure_bottom = models.PositiveSmallIntegerField(validators=[MaxValueValidator(110)],
                                                             verbose_name='Артериальное давление(нижнее,мм.рт.ст.))')
    noise_around_umbilical_area = models.CharField(max_length=150, verbose_name='Шум около пупочной области',
                                                   choices=NOICE_AROUND)
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'cardiovascular_system'
        verbose_name = 'Сердечно сосудистая система'
        verbose_name_plural = 'Сердечно сосудистая система'


# Система пищеварения(Sistema digestivus)
class DigestiveSystem(models.Model):
    STOOLS = (
        ('регулярный', 'регулярный'),
        ('запоры', 'запоры'),
        ('жидкий', 'жидкий'),
    )
    oral_musosa = models.CharField(max_length=150, verbose_name='Слизистая полоса рта')
    teeth = models.CharField(max_length=150, verbose_name='Зубы')
    tongue = models.CharField(max_length=150, verbose_name='Язык')
    pharynx = models.CharField(max_length=150, verbose_name='Зев')
    tonsils = models.CharField(max_length=150, verbose_name='Миндалины')
    stomach = models.CharField(max_length=150, verbose_name='Живот')

    liver = models.CharField(max_length=150, verbose_name='ПЕЧЕНЬ(По Курлову)')
    lower_midclavicularline = models.CharField(max_length=150, verbose_name='нижняя по среднеключичной линии ',
                                               null=True, blank=True)
    left_costal_arch = models.CharField(max_length=150, verbose_name='левой реберной дуге', null=True, blank=True)
    palpation_edge = models.CharField(max_length=150, verbose_name='при пальпации: края', null=True, blank=True)
    surface = models.CharField(max_length=150, verbose_name='при пальпации: поверхность', null=True, blank=True)
    soreness = models.CharField(max_length=150, verbose_name='при пальпации:  болезненость', null=True, blank=True)
    consistency = models.CharField(max_length=150, verbose_name='при пальпации:  консистенция', null=True, blank=True)

    gallbladder = models.CharField(max_length=150, verbose_name='Желчный пузырь')
    pancreas = models.CharField(max_length=150, verbose_name='Поджелудочная железа')

    spleen = models.CharField(max_length=150, verbose_name='Селезенка')
    boundaries = models.CharField(max_length=150, verbose_name='Границы')
    bottom_line = models.CharField(max_length=150, verbose_name='нижняя граница')
    on_palpation_edbe = models.CharField(max_length=150, verbose_name='при пальпации: края')
    bl_surface = models.CharField(max_length=150, verbose_name='при пальпации: поверхность')
    bl_tenderness = models.CharField(max_length=150, verbose_name='при пальпации:  болезненность')
    bl_consistency = models.CharField(max_length=150, verbose_name='при пальпации:  консистенция')

    stools = models.CharField(max_length=150, verbose_name='Стул (со слов пациента)',choices=STOOLS)
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'digestive_system'
        verbose_name = 'Система пищеварения'
        verbose_name_plural = 'Система пищеварения'


# Мочеполовая система(Sistema urogenitals)
class GenitoUrinarySystem(models.Model):
    URINATION_COLOR=(
        ('прозрачная', 'прозрачная'),
        ('мутная', 'мутная'),
        ('темная', 'темная'),
    )
    URINATION_QUAN=(
        ('в норме', 'в норме'),
        ('много', 'много'),
        ('мало', 'мало'),
        ('практически отсутствует', 'практически отсутствует'),
    )
    TAPPING =(
        ('отрицательно', 'отрицательно'),
        ('положительно: справа', 'положительно: справа'),
        ('положительно: слева', 'положительно: справа'),
    )

    TAPPING = (
        ('не пальпируется', 'не пальпируется'),
        ('пальпируется: болезненно', 'пальпируется: болезненно'),
        ('пальпируется: терпимо', 'пальпируется: терпимо'),
        ('пальпируется: неболезненно', 'пальпируется: неболезненно'),
    )
    urination = models.CharField(max_length=150, verbose_name='Мочеиспускание', null=True)
    urination_color = models.CharField(max_length=150, verbose_name='Моча(со слов больного)', choices=URINATION_COLOR ,null=True)
    urination_quan = models.CharField(max_length=150, verbose_name='Количество(со слов пациента)',choices=URINATION_QUAN, null=True)
    symptoms_tapping_edge_12 = models.CharField(max_length=150, verbose_name='Симптомы покалывания по  ребру',
                                                choices=TAPPING,
                                                null=True)
    palpation_kidneys = models.CharField(max_length=150, verbose_name='Пальпация почек', null=True)
    urinary_bladder = models.CharField(max_length=150, verbose_name='Мочевой пузырь', null=True)
    genitals = models.TextField(verbose_name='Половые органы', null=True)
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'genito_urinary_system'
        verbose_name = 'Мочеполовая система'
        verbose_name_plural = 'Мочеполовая система'


# Эндокринная система(Sistema endocrinologicus)
class EndocrineSystem(models.Model):
    thyroid_gland = models.CharField(max_length=150, verbose_name='Щитовидная железа')
    eye_symptoms = models.CharField(max_length=150, verbose_name='Глазные симптомы')
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'endocrine_system'
        verbose_name = 'Эндокринная система'
        verbose_name_plural = 'Эндокринная система'


# Нервно-психологическая система(Sistema neuropsychicus)
class NeuroPsychologicalSystem(models.Model):
    NEUROLOGICAL_STATUS = (
        ('воспринимает хорошо', 'воспринимает хорошо'),
        ('снижено', 'снижено'),
        ('утрачено', 'утрачено'),
    )

    FUNCTIONS_PELVICORGAN = (
        ('сохранены', 'сохранены'),
        ('нарушены', 'нарушены'),
    )
    PARKINSONISM_SYNDROME = (
        ('отсутствует', 'отсутствует'),
        ('дрожательная', 'дрожательная'),
        ('дрожательно – ригидная', 'дрожательно – ригидная'),
        ('ригидно – дрожательная', 'ригидно – дрожательная'),
        ('акинетико – ригидная', 'акинетико – ригидная'),
        ('смешанная', 'смешанная'),
    )

    EYE_SLITS=(
        ('одинаковые', 'одинаковые'),
        ('двухсторонный птоз', 'двухсторонный птоз'),
        ('левосторонный птоз', 'левосторонный птоз'),
        ('правостононный птоз', 'правостононный птоз'),
        ('левосторонный полуптоз', 'левосторонный полуптоз'),
        ('правосторонный полуптоз', 'правосторонний полуптоз'),
    )
    consciousness = models.CharField(max_length=150, verbose_name='Сознание')
    neurological_status = models.CharField(max_length=150, verbose_name='Неврологический статус',
                                           choices=NEUROLOGICAL_STATUS)
    eye_slits = models.CharField(max_length=150, verbose_name='Глазные щели')
    pupils = models.CharField(max_length=150, verbose_name='Зрачки')
    movement_eyeballs = models.CharField(max_length=150, verbose_name='Движения глазных яблок')
    face = models.CharField(max_length=150, verbose_name='Лицо')
    dizziness = models.CharField(max_length=150, verbose_name='Головокружение')
    swallowing = models.CharField(max_length=150, verbose_name='Глотание')
    protrude_tongue = models.CharField(max_length=150, verbose_name='Язык при высовывании')
    superficial_deepreflexes = models.CharField(max_length=150, verbose_name='Поверхностные и глубокие рефлексы',
                                                null=True)
    muscle_tone = models.CharField(max_length=150, verbose_name='Мышечный тонус', null=True)
    muscle_strength = models.CharField(max_length=150, verbose_name='Мышечная сила', null=True)
    sensitivity = models.CharField(max_length=150, verbose_name='Чувствительность', null=True)
    parkinsonism_syndrome = models.CharField(max_length=150, verbose_name='Синдром Паркинсонизма',
                                             choices=PARKINSONISM_SYNDROME)
    functions_pelvicorgan = models.CharField(max_length=150,
                                             verbose_name='Функции тазовых органов',
                                             choices=FUNCTIONS_PELVICORGAN)
    meningeal_symptoms = models.CharField(max_length=150, verbose_name='Менингеальные Симптомы')
    symptom_Kerning = models.CharField(max_length=150, verbose_name='Симптом Кернинг')
    memory = models.CharField(max_length=150, verbose_name='Память')
    intellect = models.CharField(max_length=150, verbose_name='Интеллект')
    valetudinarianism = models.CharField(max_length=150, verbose_name='Мнительность')
    suggestibility = models.CharField(max_length=150, verbose_name='Внушаемость')
    pathological_reflexes = models.CharField(max_length=150, verbose_name='Патологические рефлексы')
    dermographism = models.CharField(max_length=150, verbose_name='Дермографизм')
    romberg = models.CharField(max_length=150, verbose_name='В позе Ромберга')
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'neuro_psychological_system'
        verbose_name = 'Нервно-психологическая система'
        verbose_name_plural = 'Нервно-психологическая система'


# Статус локалис(Status localis)
class StatusLocalis(models.Model):
    outpatient_studies = models.TextField(verbose_name='Данные амбулаторного исследования')
    date_doctor = models.DateField(verbose_name='Дата врача', auto_now=True)  # datetime.now()
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'status_localis'
        verbose_name = 'Статус локалис'
        verbose_name_plural = 'Статус локалис'


class PlanSurvey(models.Model):
    plan_survey = models.TextField(verbose_name='План обследования')
    history = models.OneToOneField(HistoryPatientLife, null=True)

    class Meta:
        db_table = 'plan_survey'
        verbose_name = 'План обследования'
        verbose_name_plural = 'План обследования'
