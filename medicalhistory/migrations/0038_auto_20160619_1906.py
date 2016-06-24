# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0037_auto_20160619_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respiratorysystem',
            name='mobility_bottom_lungs',
            field=models.CharField(choices=[('\u0432 \u043d\u043e\u0440\u043c\u0435', '\u0432 \u043d\u043e\u0440\u043c\u0435'), ('\u043d\u0430 \u043e\u0434\u043d\u043e \u0440\u0435\u0431\u0440\u043e', '\u043d\u0430 \u043e\u0434\u043d\u043e \u0440\u0435\u0431\u0440\u043e'), ('\u043d\u0430 \u0434\u0432\u0430 \u0440\u0435\u0431\u0440\u0430', '\u043d\u0430 \u043e\u0434\u043d\u043e \u0440\u0435\u0431\u0440\u043e'), ('\u043d\u0430 \u0442\u0440\u0438 \u0440\u0435\u0431\u0440\u0430', '\u043d\u0430 \u043e\u0434\u043d\u043e \u0440\u0435\u0431\u0440\u043e')], max_length=150, verbose_name='\u041f\u043e\u0434\u0432\u0438\u0436\u043d\u043e\u0441\u0442\u044c \u043d\u0438\u0436\u043d\u0435\u0433\u043e \u043a\u0440\u0430\u044f \u043b\u0435\u0433\u043a\u0438\u0445'),
        ),
        migrations.AlterField(
            model_name='respiratorysystem',
            name='percussion_lung',
            field=models.CharField(choices=[('\u043b\u0435\u0433\u043e\u0447\u043d\u044b\u0439 \u0437\u0432\u0443\u043a(\u043d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u044b\u0439)', '\u043b\u0435\u0433\u043e\u0447\u043d\u044b\u0439 \u0437\u0432\u0443\u043a(\u043d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u044b\u0439)'), ('\u043a\u043e\u0440\u043e\u0431\u043e\u0447\u043d\u044b\u0439', '\u043a\u043e\u0440\u043e\u0431\u043e\u0447\u043d\u044b\u0439'), ('\u043f\u0440\u0438\u0442\u0443\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0440\u0430\u0432\u0430', '\u043f\u0440\u0438\u0442\u0443\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u043f\u0440\u0430\u0432\u0430'), ('\u043f\u0440\u0438\u0442\u0443\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u043b\u0435\u0432\u0430', '\u043f\u0440\u0438\u0442\u0443\u043f\u043b\u0435\u043d\u043d\u044b\u0439 \u0441\u043b\u0435\u0432\u0430')], max_length=150, verbose_name='\u041f\u0435\u0440\u043a\u0443\u0441\u0441\u0438\u044f \u043b\u0435\u0433\u043a\u0438\u0445'),
        ),
    ]
