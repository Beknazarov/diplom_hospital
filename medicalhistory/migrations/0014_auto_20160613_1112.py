# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 05:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0013_auto_20160613_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuslocalis',
            name='date_doctor',
            field=models.DateField(default=datetime.datetime(2016, 6, 13, 11, 12, 38, 847577), verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0440\u0430\u0447\u0430'),
        ),
    ]
