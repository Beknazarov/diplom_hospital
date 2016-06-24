# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 09:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0021_auto_20160613_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='between_ribs',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(7)], verbose_name='\u041c\u0435\u0436\u0440\u0435\u0431\u0440\u0438\u0435'),
        ),
    ]