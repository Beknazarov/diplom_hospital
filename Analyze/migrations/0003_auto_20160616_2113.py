# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Analyze', '0002_auto_20160612_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodchemistry',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KIF.Doctor', verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='genbloodanalyse',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KIF.Doctor', verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='ptianalysis',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KIF.Doctor', verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440'),
        ),
        migrations.AlterField(
            model_name='urineanalysis',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KIF.Doctor', verbose_name='\u0414\u043e\u043a\u0442\u043e\u0440'),
        ),
    ]