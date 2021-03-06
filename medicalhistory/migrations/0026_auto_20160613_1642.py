# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0025_auto_20160613_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='left_bound_heart',
            field=models.CharField(max_length=150, verbose_name='\u041b\u0435\u0432\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0441\u0435\u0440\u0434\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='right_bound_heart',
            field=models.CharField(max_length=150, verbose_name='\u041f\u0440\u0430\u0432\u0430\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0441\u0435\u0440\u0434\u0446\u0430'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='top_bound_heart',
            field=models.CharField(max_length=150, verbose_name='\u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0441\u0435\u0440\u0434\u0446\u0430'),
        ),
    ]
