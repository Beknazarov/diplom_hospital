# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 05:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0030_auto_20160616_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='senses',
            old_name='senses',
            new_name='senses_cond',
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='aorta',
            field=models.CharField(choices=[('II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d', 'II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d'), ('\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d', '\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d'), ('\u0430\u043a\u0446\u0435\u043d\u0442', '\u0430\u043a\u0446\u0435\u043d\u0442')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u043d\u0430 \u0430\u043e\u0440\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='arteries',
            field=models.CharField(choices=[('\u043f\u0443\u043b\u044c\u0441\u0430\u0446\u0438\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0435 \u0432 \u043d\u043e\u0440\u043c\u0435', '\u043f\u0443\u043b\u044c\u0441\u0430\u0446\u0438\u044f \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0435 \u0432 \u043d\u043e\u0440\u043c\u0435'), ('\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e', '\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e'), ('\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d\u0430', '\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d\u0430')], max_length=150, verbose_name='\u0410\u0440\u0442\u0435\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='ausculation_heart_top',
            field=models.CharField(choices=[('II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d', 'II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d'), ('\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d', '\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d'), ('\u0430\u043a\u0446\u0435\u043d\u0442', '\u0430\u043a\u0446\u0435\u043d\u0442')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430: \u043d\u0430 \u0432\u0435\u0440\u0445\u0443\u0448\u043a\u0435'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='flap_3_valve',
            field=models.CharField(choices=[('\u0448\u0443\u043c\u043e\u0432 \u043d\u0435\u0442', '\u0448\u0443\u043c\u043e\u0432 \u043d\u0435\u0442'), ('\u0441\u043b\u0430\u0431\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430', '\u0441\u043b\u0430\u0431\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430'), ('\u0441\u0438\u043b\u044c\u043d\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430', '\u0441\u043b\u0430\u0431\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u043d\u0430 3-\u0445 \u0441\u0442\u0432\u043e\u0440\u0447\u0430\u0442\u043e\u043c \u043a\u043b\u0430\u043f\u0430\u043d\u0435'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='in_pulmonary_artery',
            field=models.CharField(choices=[('II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d', 'II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d'), ('\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d', '\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d'), ('\u0430\u043a\u0446\u0435\u043d\u0442', '\u0430\u043a\u0446\u0435\u043d\u0442')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u043d\u0430 \u043b\u0435\u0433\u043e\u0447\u043d\u043e\u0439 \u0430\u0440\u0442\u0435\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='left_ebge_sternum',
            field=models.CharField(choices=[('II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d', 'II \u0442\u043e\u043d \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d'), ('\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d', '\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d'), ('\u0430\u043a\u0446\u0435\u043d\u0442', '\u0430\u043a\u0446\u0435\u043d\u0442')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u041f\u043e \u043b\u0435\u0432\u043e\u043c\u0443 \u043a\u0440\u0430\u044e \u0433\u0440\u0443\u0434\u0438\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='noise_around_umbilical_area',
            field=models.CharField(choices=[('\u0448\u0443\u043c\u043e\u0432 \u043d\u0435\u0442', '\u0448\u0443\u043c\u043e\u0432 \u043d\u0435\u0442'), ('\u0441\u043b\u0430\u0431\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430', '\u0441\u043b\u0430\u0431\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430'), ('\u0441\u0438\u043b\u044c\u043d\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430', '\u0441\u043b\u0430\u0431\u043e \u0432\u044b\u0440\u0430\u0436\u0435\u043d\u0430')], max_length=150, verbose_name='\u0428\u0443\u043c \u043e\u043a\u043e\u043b\u043e \u043f\u0443\u043f\u043e\u0447\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='historypatientlife',
            name='disability_group',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '\u041f\u0435\u0440\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430'), (2, '\u0412\u0442\u043e\u0440\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430'), (3, '\u0422\u0440\u0435\u0442\u044c\u044f \u0433\u0440\u0443\u043f\u043f\u0430')], validators=[django.core.validators.MaxValueValidator(3)], verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u0438\u043d\u0432\u0430\u043b\u0438\u0434\u043d\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='historypatientlife',
            name='social_conditions',
            field=models.CharField(choices=[('\u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435', '\u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435'), ('\u043d\u0435\u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435', '\u043d\u0435\u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435'), ('\u0445\u043e\u0440\u043e\u0448\u0438\u0435', '\u0445\u043e\u0440\u043e\u0448\u0438\u0435')], max_length=150, verbose_name='\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e \u0431\u044b\u0442\u043e\u0432\u044b\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='neuropsychologicalsystem',
            name='functions_pelvicorgan',
            field=models.CharField(choices=[('\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u044b', '\u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u044b'), ('\u043d\u0430\u0440\u0443\u0448\u0435\u043d\u044b', '\u043d\u0430\u0440\u0443\u0448\u0435\u043d\u044b')], max_length=150, verbose_name='\u0424\u0443\u043d\u043a\u0446\u0438\u0438 \u0442\u0430\u0437\u043e\u0432\u044b\u0445 \u043e\u0440\u0433\u0430\u043d\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='neuropsychologicalsystem',
            name='neurological_status',
            field=models.CharField(choices=[('\u0432\u043e\u0441\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0445\u043e\u0440\u043e\u0448\u043e', '\u0432\u043e\u0441\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442 \u0445\u043e\u0440\u043e\u0448\u043e'), ('\u0441\u043d\u0438\u0436\u0435\u043d\u043e', '\u0441\u043d\u0438\u0436\u0435\u043d\u043e'), ('\u0443\u0442\u0440\u0430\u0447\u0435\u043d\u043e', '\u0443\u0442\u0440\u0430\u0447\u0435\u043d\u043e')], max_length=150, verbose_name='\u041d\u0435\u0432\u0440\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441'),
        ),
        migrations.AlterField(
            model_name='neuropsychologicalsystem',
            name='parkinsonism_syndrome',
            field=models.CharField(choices=[('\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442', '\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442'), ('\u0434\u0440\u043e\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f', '\u0434\u0440\u043e\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f'), ('\u0434\u0440\u043e\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u2013 \u0440\u0438\u0433\u0438\u0434\u043d\u0430\u044f', '\u0434\u0440\u043e\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u2013 \u0440\u0438\u0433\u0438\u0434\u043d\u0430\u044f'), ('\u0440\u0438\u0433\u0438\u0434\u043d\u043e \u2013 \u0434\u0440\u043e\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f', '\u0440\u0438\u0433\u0438\u0434\u043d\u043e \u2013 \u0434\u0440\u043e\u0436\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f'), ('\u0430\u043a\u0438\u043d\u0435\u0442\u0438\u043a\u043e \u2013 \u0440\u0438\u0433\u0438\u0434\u043d\u0430\u044f', '\u0430\u043a\u0438\u043d\u0435\u0442\u0438\u043a\u043e \u2013 \u0440\u0438\u0433\u0438\u0434\u043d\u0430\u044f'), ('\u0441\u043c\u0435\u0448\u0430\u043d\u043d\u0430\u044f', '\u0441\u043c\u0435\u0448\u0430\u043d\u043d\u0430\u044f')], max_length=150, verbose_name='\u0421\u0438\u043d\u0434\u0440\u043e\u043c \u041f\u0430\u0440\u043a\u0438\u043d\u0441\u043e\u043d\u0438\u0437\u043c\u0430'),
        ),
        migrations.AlterField(
            model_name='patientconditionsnow',
            name='body',
            field=models.CharField(blank=True, choices=[('\u0430\u0441\u0442\u0435\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435', '\u0430\u0441\u0442\u0435\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435'), ('\u043d\u043e\u0440\u043c\u043e\u0441\u0442\u0435\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435', '\u043d\u043e\u0440\u043c\u043e\u0441\u0442\u0435\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435'), ('\u0433\u0438\u043f\u0435\u0440\u0441\u0442\u0435\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435', '\u0433\u0438\u043f\u0435\u0440\u0441\u0442\u0435\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435')], max_length=100, verbose_name='\u0422\u0435\u043b\u043e\u0441\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='patientconditionsnow',
            name='position',
            field=models.CharField(blank=True, choices=[('\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435', '\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435'), ('\u0432\u044b\u043d\u0443\u0436\u0434\u0435\u043d\u043d\u043e\u0435', '\u0432\u044b\u043d\u0443\u0436\u0434\u0435\u043d\u043d\u043e\u0435')], max_length=150, verbose_name='\u041f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='respiratorysystem',
            name='omision_lower_bound',
            field=models.CharField(choices=[('\u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0432 \u043d\u043e\u0440\u043c\u0435', '\u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0435 \u0441 \u043e\u0431\u0435\u0438\u0445 \u0441\u0442\u043e\u0440\u043e\u043d'), ('\u043e\u043f\u0443\u0449\u0435\u043d\u043e \u043d\u0430 \u043e\u0434\u043d\u043e \u0440\u0435\u0431\u0440\u043e', '\u043e\u043f\u0443\u0449\u0435\u043d\u043e \u043d\u0430 \u043e\u0434\u043d\u043e \u0440\u0435\u0431\u0440\u043e'), ('\u043e\u043f\u0443\u0449\u0435\u043d\u043e \u043d\u0430 \u0434\u0432\u0430 \u0440\u0435\u0431\u0440\u0430', '\u043e\u043f\u0443\u0449\u0435\u043d\u043e \u043d\u0430 \u0434\u0432\u0430 \u0440\u0435\u0431\u0440\u0430')], max_length=150, verbose_name='\u041e\u043f\u0443\u0449\u0435\u043d\u0438\u0435 \u043d\u0438\u0436\u043d\u0438\u0445 \u0433\u0440\u0430\u043d\u0438\u0446'),
        ),
        migrations.AlterField(
            model_name='respiratorysystem',
            name='part_chest_breathing',
            field=models.CharField(blank=True, choices=[('\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e', '\u0441\u0438\u043c\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e'), ('\u043e\u0442\u0441\u0442\u0430\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430', '\u043e\u0442\u0441\u0442\u0430\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430'), ('\u043e\u0442\u0441\u0442\u0430\u0435\u0442 \u0441\u043b\u0435\u0432\u0430', '\u043e\u0442\u0441\u0442\u0430\u0435\u0442 \u0441\u043b\u0435\u0432\u0430')], max_length=40, verbose_name='\u0423\u0447\u0430\u0441\u0442\u0438\u0435 \u0433\u0440\u0443\u0434\u043d\u043e\u0439 \u043a\u043b\u0435\u0442\u043a\u0438 \u0432 \u0430\u043a\u0442\u0435 \u0434\u044b\u0445\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='respiratorysystem',
            name='voice_tremor',
            field=models.CharField(choices=[('\u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0435 \u0441 \u043e\u0431\u0435\u0438\u0445 \u0441\u0442\u043e\u0440\u043e\u043d', '\u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0435 \u0441 \u043e\u0431\u0435\u0438\u0445 \u0441\u0442\u043e\u0440\u043e\u043d'), ('\u0443\u0441\u0438\u043b\u0435\u043d\u043e', '\u0443\u0441\u0438\u043b\u0435\u043d\u043e'), ('\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d\u043e', '\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d\u043e')], max_length=150, verbose_name='\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u043e\u0435 \u0434\u0440\u043e\u0436\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='women',
            name='mensrtuation_regularity',
            field=models.CharField(blank=True, choices=[('\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435', '\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435'), ('\u043d\u0435\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435', '\u043d\u0435\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0435')], max_length=50, null=True, verbose_name='\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0435(\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c)'),
        ),
        migrations.AlterField(
            model_name='women',
            name='menstruation_ache',
            field=models.CharField(blank=True, choices=[('\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u043e', '\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u043e'), ('\u043d\u0435\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u043e', '\u043d\u0435\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u043e')], max_length=50, null=True, verbose_name='\u041c\u0435\u0441\u044f\u0447\u043d\u044b\u0435(\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u043e\u0441\u0442\u044c)'),
        ),
    ]