# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0031_auto_20160616_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historypatientlife',
            name='recordpatient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='KIF.RecordPatient', verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442'),
        ),
    ]
