# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Справочники

# HistoryPatientLife

class risk_factor(models.Model):
    type = models.CharField(max_length=100, verbose_name='Фактор риска', blank=True)

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'risk_factor_types'
        verbose_name_plural = 'Факторы риска'
        verbose_name = 'Фактор риска'


# Women
class menstruation(models.Model):
    type = models.CharField(max_length=120, verbose_name='Тип менструации')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'menstruation_types'
        verbose_name_plural = 'Течение менструации'
        verbose_name = 'Течение менструации'


class pregnancy_proceeds(models.Model):
    type = models.CharField(max_length=150, verbose_name='Тип протекания беременности')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'pregnancy_proceeds_types'
        verbose_name_plural = 'Течение беременности'
        verbose_name = 'Течение беременности'


class mammary_gland(models.Model):
    type = models.CharField(max_length=150, verbose_name='Молочные железы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'mammary_gland_types'
        verbose_name_plural = 'Молочные железы'
        verbose_name = 'Молочные железы'


# PatientConditionsNow
class general_state(models.Model):
    type = models.CharField(max_length=150, verbose_name='Общее состояние')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'general_state_types'
        verbose_name_plural = 'Общее состояние'
        verbose_name = 'Общее состояние'


class skin(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тип кожных покровов', blank=True)

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'skin_types'
        verbose_name_plural = 'Кожные покровы'
        verbose_name = 'Кожные покровы'


class subcutaneous_tissue(models.Model):
    type = models.CharField(max_length=100, verbose_name='Тип подкожной клетчатки', blank=True)

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'subcutaneous_tissue_types'
        verbose_name_plural = 'Тип подкожной клетчатки'
        verbose_name = 'Тип подкожной клетчатки'


class nails(models.Model):
    type = models.CharField(max_length=150, verbose_name='Тип ногтей')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'nails_types'
        verbose_name_plural = 'Ногти'
        verbose_name = 'Ногти'


class muscles(models.Model):
    type = models.CharField(max_length=150, verbose_name='Тип мыщцы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'muscles_types'
        verbose_name_plural = 'Мышцы'
        verbose_name = 'Мышцы'


class bones(models.Model):
    type = models.CharField(max_length=150, verbose_name='Тип костей')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'bones_types'
        verbose_name_plural = 'Кости'
        verbose_name = 'Кости'


class joints(models.Model):
    type = models.CharField(max_length=150, verbose_name='Тип суставов')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'joints_types'
        verbose_name_plural = 'Суставы'
        verbose_name = 'Суставы'


class lymph_node(models.Model):
    type = models.CharField(max_length=150, verbose_name='Лимфатические узлы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'lymphnode_types'
        verbose_name_plural = 'Лимфатические узлы'
        verbose_name = 'Лимфатические узлы'


# Senses
class senses_cond(models.Model):
    type = models.CharField(max_length=150, verbose_name='Органы чусвтв')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'senses_cond_types'
        verbose_name_plural = 'Органы чусвтв'
        verbose_name = 'Органы чусвтв'


class eyes(models.Model):
    type = models.CharField(max_length=150, verbose_name='Глаза')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'eyes_types'
        verbose_name_plural = 'Глаза'
        verbose_name = 'Глаза'


class hearing(models.Model):
    type = models.CharField(max_length=150, verbose_name='Слух')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'hearing_types'
        verbose_name_plural = 'Слух'
        verbose_name = 'Слух'


class skin_sensitivity(models.Model):
    type = models.CharField(max_length=150, verbose_name='Чувствительность  кожных покровов')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'skin_sensitivity_types'
        verbose_name_plural = 'Чувствительность  кожных покровов'
        verbose_name = 'Чувствительность  кожных покровов'


class smell(models.Model):
    type = models.CharField(max_length=150, verbose_name='Обоняние')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'smell_types'
        verbose_name_plural = 'Обоняние'
        verbose_name = 'Обоняние'


# RespiratorySystem


class nasal_breathing(models.Model):
    type = models.CharField(max_length=150, verbose_name='Носовое дыхание')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'nasal_breathing_types'
        verbose_name_plural = 'Носовое дыхание'
        verbose_name = 'Носовое дыхание'


class rib_cage(models.Model):
    type = models.CharField(max_length=150, verbose_name='Грудная клетка')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'rib_cage_types'
        verbose_name_plural = 'Грудная клетка'
        verbose_name = 'Грудная клетка'


class part_chest_breathing(models.Model):
    type = models.CharField(max_length=150, verbose_name='Участие грудной клетки в акте дыхания')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'part_chest_breathing_types'
        verbose_name_plural = 'Участие грудной клетки в акте дыхания'
        verbose_name = 'Участие грудной клетки в акте дыхания'


class part_breathing_muscle(models.Model):
    type = models.CharField(max_length=150, verbose_name='Участие в акте дыхания мышц')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'part_breathing_muscle_types'
        verbose_name_plural = 'Участие в акте дыхания мышц'
        verbose_name = 'Участие в акте дыхания мышц'


class percussion_lung(models.Model):
    type = models.CharField(max_length=150, verbose_name='Перкуссия легких')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'percussion_lung_types'
        verbose_name_plural = 'Перкуссия легких'
        verbose_name = 'Перкуссия легких'


class omision_lower_bound(models.Model):
    type = models.CharField(max_length=150, verbose_name='Опущение нижних границ')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'omision_lower_bound_types'
        verbose_name_plural = 'Опущение нижних границ'
        verbose_name = 'Опущение нижних границ'


class mobility_bottom_lungs(models.Model):
    type = models.CharField(max_length=150, verbose_name='Подвижность нижнего края легких')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'mobility_bottom_lungs_types'
        verbose_name_plural = 'Подвижность нижнего края легких'
        verbose_name = 'Подвижность нижнего края легких'


class auscultation_lungs(models.Model):
    type = models.CharField(max_length=150, verbose_name='Аускультация легких')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'auscultation_lungs_types'
        verbose_name_plural = 'Аускультация легких:дыхание'
        verbose_name = 'Аускультация легких:дыхание'


class wheezing(models.Model):
    type = models.CharField(max_length=150, verbose_name='Хрипы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'wheezing_types'
        verbose_name_plural = 'Хрипы'
        verbose_name = 'Хрипы'


class breathing_rhythm(models.Model):
    type = models.CharField(max_length=150, verbose_name='Ритм дыхания')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'breathing_rhythm_types'
        verbose_name_plural = 'Ритм дыхания'
        verbose_name = 'Ритм дыхания'


# CardiovascularSystem
class when_viewed(models.Model):
    type = models.CharField(max_length=150, verbose_name='При осмотре')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'when_viewed_types'
        verbose_name_plural = 'При осмотре'
        verbose_name = 'При осмотре'


class epigastric_pulsation(models.Model):
    type = models.CharField(max_length=150, verbose_name='Эпигастральная пальпация')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'epigastric_pulsation_types'
        verbose_name_plural = 'Эпигастральная пальпация'
        verbose_name = 'Эпигастральная пальпация'


class visible_heart_pulsation(models.Model):
    type = models.CharField(max_length=150, verbose_name='Видимые на глаз сердечные пульсации')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'visible_heart_pulsation_types'
        verbose_name_plural = 'Видимые на глаз сердечные пульсации'
        verbose_name = 'Видимые на глаз сердечные пульсации'


class cyanosis(models.Model):
    type = models.CharField(max_length=150, verbose_name='Цианоз')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'cyanosis_types'
        verbose_name_plural = 'Цианоз'
        verbose_name = 'Цианоз'


class apical_impulse(models.Model):
    type = models.CharField(max_length=150, verbose_name='Верхушечный толчок')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'apical_impulse_types'
        verbose_name_plural = 'Верхушечный толчок'
        verbose_name = 'Верхушечный толчок'


class flap_3_valve(models.Model):
    type = models.CharField(max_length=150, verbose_name='на 3-х створчатом клапане')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'flap_3_valve_types'
        verbose_name_plural = 'на 3-х створчатом клапане'
        verbose_name = 'на 3-х створчатом клапане'


class left_ebge_sternum(models.Model):
    type = models.CharField(max_length=150, verbose_name='По левому краю грудины')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'left_ebge_sternum_types'
        verbose_name_plural = 'По левому краю грудины'
        verbose_name = 'По левому краю грудины'


class arteries(models.Model):
    type = models.CharField(max_length=150, verbose_name='Артерии')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'arteries_types'
        verbose_name_plural = 'Артерии'
        verbose_name = 'Артерии'


class vien(models.Model):
    type = models.CharField(max_length=150, verbose_name='Вены')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'vien_types'
        verbose_name_plural = 'Вены'
        verbose_name = 'Вены'


class pulse_rhythm(models.Model):
    type = models.CharField(max_length=150, verbose_name='Пульс-Ритм')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'pulse_rhythm_types'
        verbose_name_plural = 'Пульс-Ритм'
        verbose_name = 'Пульс-Ритм'


class pulse_deficit(models.Model):
    type = models.CharField(max_length=150, verbose_name='Дефицит пульса')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'pulse_deficit_types'
        verbose_name_plural = 'Дефицит пульса'
        verbose_name = 'Дефицит пульса'


# DigestiveSystem


class oral_musosa(models.Model):
    type = models.CharField(max_length=150, verbose_name='Слизистая полоса рта')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'oral_musosa_types'
        verbose_name_plural = 'Слизистая полоса рта'
        verbose_name = 'Слизистая полоса рта'


class teeth(models.Model):
    type = models.CharField(max_length=150, verbose_name='Зубы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'teeth_types'
        verbose_name_plural = 'Зубы'
        verbose_name = 'Зубы'


class tongue(models.Model):
    type = models.CharField(max_length=150, verbose_name='Язык')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'tongue_types'
        verbose_name_plural = 'Язык'
        verbose_name = 'Язык'


class pharynx(models.Model):
    type = models.CharField(max_length=150, verbose_name='Зев')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'pharynx_types'
        verbose_name_plural = 'Зев'
        verbose_name = 'Зев'


class tonsils(models.Model):
    type = models.CharField(max_length=150, verbose_name='Миндалины')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'tonsils_types'
        verbose_name_plural = 'Миндалины'
        verbose_name = 'Миндалины'


class stomach(models.Model):
    type = models.CharField(max_length=150, verbose_name='Живот')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'stomach_types'
        verbose_name_plural = 'Живот'
        verbose_name = 'Живот'


class liver(models.Model):
    type = models.CharField(max_length=150, verbose_name='Печень(По Курлову)')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'liver_types'
        verbose_name_plural = 'Печень'
        verbose_name = 'Печень'


class lower_midclavicularline(models.Model):
    type = models.CharField(max_length=150, verbose_name='нижняя по среднеключичной линии')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'lower_midclavicularline_types'
        verbose_name_plural = 'нижняя по среднеключичной линии'
        verbose_name = 'нижняя по среднеключичной линии'


class left_costal_arch(models.Model):
    type = models.CharField(max_length=150, verbose_name='нижняя по среднеключичной линии')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'left_costal_arch_types'
        verbose_name_plural = 'левой реберной дуге'
        verbose_name = 'левой реберной дуге'


class palpation_edge(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации: края')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'palpation_edge_types'
        verbose_name_plural = 'при пальпации: края'
        verbose_name = 'при пальпации: края'


class surface(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации: поверхность')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'surface_types'
        verbose_name_plural = 'при пальпации: поверхность'
        verbose_name = 'при пальпации: поверхность'


class soreness(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации:  болезненость')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'soreness_types'
        verbose_name_plural = 'при пальпации:  болезненость'
        verbose_name = 'при пальпации:  болезненость'


class consistency(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации:  консистенция')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'consistency_types'
        verbose_name_plural = 'при пальпации:  консистенция'
        verbose_name = 'при пальпации:  консистенция'


class gallbladder(models.Model):
    type = models.CharField(max_length=150, verbose_name='Желчный пузырь')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'gallbladder_types'
        verbose_name_plural = 'Желчный пузырь'
        verbose_name = 'Желчный пузырь'


class pancreas(models.Model):
    type = models.CharField(max_length=150, verbose_name='Поджелудочная железа')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'pancreas_types'
        verbose_name_plural = 'Поджелудочная железа'
        verbose_name = 'Поджелудочная железа'


class spleen(models.Model):
    type = models.CharField(max_length=150, verbose_name='Селезенка')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'spleen_types'
        verbose_name_plural = 'Селезенка'
        verbose_name = 'Селезенка'


class boundaries(models.Model):
    type = models.CharField(max_length=150, verbose_name='Границы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'boundaries_types'
        verbose_name_plural = 'Границы'
        verbose_name = 'Границы'


class bottom_line(models.Model):
    type = models.CharField(max_length=150, verbose_name='нижняя граница')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'bottom_line_types'
        verbose_name_plural = 'нижняя граница'
        verbose_name = 'нижняя граница'


class on_palpation_edbe(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации: края')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'on_palpation_edbe_types'
        verbose_name_plural = 'при пальпации: края'
        verbose_name = 'при пальпации: края'


class bl_surface(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации: поверхность')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'bl_surface_types'
        verbose_name_plural = 'при пальпации: поверхность'
        verbose_name = 'при пальпации: поверхность'


class bl_tenderness(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации:  болезненность')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'bl_tenderness_types'
        verbose_name_plural = 'при пальпации:  болезненность'
        verbose_name = 'при пальпации:  болезненность'


class bl_consistency(models.Model):
    type = models.CharField(max_length=150, verbose_name='при пальпации:  консистенция')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'bl_consistency_types'
        verbose_name_plural = 'при пальпации:  консистенция'
        verbose_name = 'при пальпации:  консистенция'


class urinary_bladder(models.Model):
    type = models.CharField(max_length=150, verbose_name='Мочевой пузырь')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'urinary_bladder_types'
        verbose_name_plural = 'Мочевой пузырь'
        verbose_name = 'Мочевой пузырь'


class genitals(models.Model):
    type = models.CharField(max_length=150, verbose_name='Мочевой пузырь')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'genitals_types'
        verbose_name_plural = 'Мочевой пузырь'
        verbose_name = 'Мочевой пузырь'


# Sistema endocrinologicu
class thyroid_gland(models.Model):
    type = models.CharField(max_length=150, verbose_name='Щитовидная железа')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'thyroid_gland_types'
        verbose_name_plural = 'Щитовидная железа'
        verbose_name = 'Щитовидная железа'


class eye_symptoms(models.Model):
    type = models.CharField(max_length=150, verbose_name='Глазные симптомы')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'eye_symptoms_types'
        verbose_name_plural = 'Глазные симптомы'
        verbose_name = 'Глазные симптомы'


# Sistema neuropsychicus
class consciousness(models.Model):
    type = models.CharField(max_length=150, verbose_name='Сознание')

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'consciousness_types'
        verbose_name_plural = 'Сознание'
        verbose_name = 'Сознание'


class pupils(models.Model):
    type = models.CharField(max_length=150, verbose_name='Зрачки')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Зрачки'
        verbose_name = 'Зрачки'


class movement_eyeballs(models.Model):
    type = models.CharField(max_length=150, verbose_name='Движения глазных яблок')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Движения глазных яблок'
        verbose_name = 'Движения глазных яблок'


class face(models.Model):
    type = models.CharField(max_length=150, verbose_name='Лицо')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Лицо'
        verbose_name = 'Лицо'


class dizziness(models.Model):
    type = models.CharField(max_length=150, verbose_name='Головокружение')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Головокружение'
        verbose_name = 'Головокружение'


class swallowing(models.Model):
    type = models.CharField(max_length=150, verbose_name='Глотание')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Глотание'
        verbose_name = 'Глотание'


class protrude_tongue(models.Model):
    type = models.CharField(max_length=150, verbose_name='Язык при высовывании')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Язык при высовывании'
        verbose_name = 'Язык при высовывании'


class superficial_deepreflexes(models.Model):
    type = models.CharField(max_length=150, verbose_name='Поверхностные и глубокие рефлексы')

    def __unicode__(self):
        return self.type

    class Meta:

        verbose_name_plural = 'Поверхностные и глубокие рефлексы'
        verbose_name = 'Поверхностные и глубокие рефлексы'


class muscle_tone(models.Model):
    type = models.CharField(max_length=150, verbose_name='Мышечный тонус')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Мышечный тонус'
        verbose_name = 'Мышечный тонус'


class muscle_strength(models.Model):
    type = models.CharField(max_length=150, verbose_name='Мышечная сила')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Мышечная сила'
        verbose_name = 'Мышечная сила'


class sensitivity(models.Model):
    type = models.CharField(max_length=150, verbose_name='Чувствительность')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Чувствительность'
        verbose_name = 'Чувствительность'


class meningeal_symptoms(models.Model):
    type = models.CharField(max_length=150, verbose_name='Менингеальные Симптомы')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Менингеальные Симптомы'
        verbose_name = 'Менингеальные Симптомы'


class symptom_Kerning(models.Model):
    type = models.CharField(max_length=150, verbose_name='Симптом Кернинг')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Симптом Кернинг'
        verbose_name = 'Симптом Кернинг'


class memory(models.Model):
    type = models.CharField(max_length=150, verbose_name='Память')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Интеллект'
        verbose_name = 'Память'


class intellect(models.Model):
    type = models.CharField(max_length=150, verbose_name='Интеллект')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Интеллект'
        verbose_name = 'Интеллект'


class valetudinarianism(models.Model):
    type = models.CharField(max_length=150, verbose_name='Мнительность')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Мнительность'
        verbose_name = 'Мнительность'


class suggestibility(models.Model):
    type = models.CharField(max_length=150, verbose_name='Внушаемость')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Внушаемость'
        verbose_name = 'Внушаемость'


class pathological_reflexes(models.Model):
    type = models.CharField(max_length=150, verbose_name='Патологические рефлексы')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'Патологические рефлексы'
        verbose_name = 'Патологические рефлексы'


class romberg(models.Model):
    type = models.CharField(max_length=150, verbose_name='В позе Ромберга')

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name_plural = 'В позе Ромберга'
        verbose_name = 'В позе Ромберга'
