# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-11 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassMKB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('parent_code', models.CharField(blank=True, max_length=100, null=True)),
                ('node_count', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class_mkb',
            },
        ),
    ]
