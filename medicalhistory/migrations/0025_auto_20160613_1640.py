# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalhistory', '0024_auto_20160613_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='aorta',
            field=models.CharField(choices=[(b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd', b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd'), (b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd', b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd'), (b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82', b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u043d\u0430 \u0430\u043e\u0440\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='ausculation_heart_top',
            field=models.CharField(choices=[(b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd', b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd'), (b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd', b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd'), (b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82', b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430: \u043d\u0430 \u0432\u0435\u0440\u0445\u0443\u0448\u043a\u0435'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='diastolic_murmur',
            field=models.CharField(max_length=150, null=True, verbose_name='\u0414\u0438\u0430\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='flap_3_valve',
            field=models.CharField(choices=[(b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd', b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd'), (b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd', b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd'), (b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82', b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u043d\u0430 3-\u0445 \u0441\u0442\u0432\u043e\u0440\u0447\u0430\u0442\u043e\u043c \u043a\u043b\u0430\u043f\u0430\u043d\u0435'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='in_pulmonary_artery',
            field=models.CharField(choices=[(b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd', b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd'), (b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd', b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd'), (b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82', b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u043d\u0430 \u043b\u0435\u0433\u043e\u0447\u043d\u043e\u0439 \u0430\u0440\u0442\u0435\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='left_ebge_sternum',
            field=models.CharField(choices=[(b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd', b'II \xd1\x82\xd0\xbe\xd0\xbd \xd1\x81\xd0\xbe\xd1\x85\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb5\xd0\xbd'), (b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd', b'\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd'), (b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82', b'\xd0\xb0\xd0\xba\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82')], max_length=150, verbose_name='\u0410\u0443\u0441\u043a\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f \u0441\u0435\u0440\u0434\u0446\u0430:\u041f\u043e \u043b\u0435\u0432\u043e\u043c\u0443 \u043a\u0440\u0430\u044e \u0433\u0440\u0443\u0434\u0438\u043d\u044b'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='systolic_diastolic_noise',
            field=models.CharField(max_length=150, null=True, verbose_name='\u0421\u0438\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0438 \u0434\u0438\u0430\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c\u044b'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='systolic_diastolic_noise_2',
            field=models.CharField(max_length=150, null=True, verbose_name='\u0421\u0438\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0438 \u0434\u0438\u0430\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c\u044b'),
        ),
        migrations.AlterField(
            model_name='cardiovascularsystem',
            name='systolic_murmur',
            field=models.CharField(max_length=150, null=True, verbose_name='\u0421\u0438\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c'),
        ),
    ]
