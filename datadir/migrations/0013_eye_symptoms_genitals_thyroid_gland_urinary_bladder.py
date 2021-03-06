# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadir', '0012_bl_consistency_bl_surface_bl_tenderness_bottom_line_boundaries_consistency_flap_3_valve_gallbladder_'),
    ]

    operations = [
        migrations.CreateModel(
            name='eye_symptoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150, verbose_name='\u0413\u043b\u0430\u0437\u043d\u044b\u0435 \u0441\u0438\u043c\u043f\u0442\u043e\u043c\u044b')),
            ],
            options={
                'db_table': 'eye_symptoms_types',
                'verbose_name': '\u0413\u043b\u0430\u0437\u043d\u044b\u0435 \u0441\u0438\u043c\u043f\u0442\u043e\u043c\u044b',
                'verbose_name_plural': '\u0413\u043b\u0430\u0437\u043d\u044b\u0435 \u0441\u0438\u043c\u043f\u0442\u043e\u043c\u044b',
            },
        ),
        migrations.CreateModel(
            name='genitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150, verbose_name='\u041c\u043e\u0447\u0435\u0432\u043e\u0439 \u043f\u0443\u0437\u044b\u0440\u044c')),
            ],
            options={
                'db_table': 'genitals_types',
                'verbose_name': '\u041c\u043e\u0447\u0435\u0432\u043e\u0439 \u043f\u0443\u0437\u044b\u0440\u044c',
                'verbose_name_plural': '\u041c\u043e\u0447\u0435\u0432\u043e\u0439 \u043f\u0443\u0437\u044b\u0440\u044c',
            },
        ),
        migrations.CreateModel(
            name='thyroid_gland',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150, verbose_name='\u0429\u0438\u0442\u043e\u0432\u0438\u0434\u043d\u0430\u044f \u0436\u0435\u043b\u0435\u0437\u0430')),
            ],
            options={
                'db_table': 'thyroid_gland_types',
                'verbose_name': '\u0429\u0438\u0442\u043e\u0432\u0438\u0434\u043d\u0430\u044f \u0436\u0435\u043b\u0435\u0437\u0430',
                'verbose_name_plural': '\u0429\u0438\u0442\u043e\u0432\u0438\u0434\u043d\u0430\u044f \u0436\u0435\u043b\u0435\u0437\u0430',
            },
        ),
        migrations.CreateModel(
            name='urinary_bladder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150, verbose_name='\u041c\u043e\u0447\u0435\u0432\u043e\u0439 \u043f\u0443\u0437\u044b\u0440\u044c')),
            ],
            options={
                'db_table': 'urinary_bladder_types',
                'verbose_name': '\u041c\u043e\u0447\u0435\u0432\u043e\u0439 \u043f\u0443\u0437\u044b\u0440\u044c',
                'verbose_name_plural': '\u041c\u043e\u0447\u0435\u0432\u043e\u0439 \u043f\u0443\u0437\u044b\u0440\u044c',
            },
        ),
    ]
