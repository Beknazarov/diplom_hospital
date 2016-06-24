# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 05:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0012_auto_20160613_1110'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MenstruationType',
        ),
        migrations.DeleteModel(
            name='PregnancyProceedsType',
        ),
        migrations.AlterField(
            model_name='statuslocalis',
            name='date_doctor',
            field=models.DateField(default=datetime.datetime(2016, 6, 13, 11, 11, 44, 99555), verbose_name='\u0414\u0430\u0442\u0430 \u0432\u0440\u0430\u0447\u0430'),
        ),
    ]