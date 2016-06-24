# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class ClassMKB(models.Model):

    name = models.CharField(max_length=512,verbose_name = 'Наименование')
    code = models.CharField(max_length=20, null=True, blank=True,verbose_name = 'Код')
    parent_id = models.IntegerField(null=True, blank=True)
    parent_code = models.CharField(max_length=100, null=True, blank=True,verbose_name = 'Код предка')
    node_count = models.SmallIntegerField(default=0, null=True, blank=True,verbose_name = 'Количество в группе')
    additional_info = models.TextField(null=True, blank=True,verbose_name = 'Дополнительно')

    class Meta:
        db_table = 'class_mkb'
        verbose_name = 'Международная класификация болезней'
        verbose_name_plural = 'Международная класификация болезней'

    def __unicode__(self):
        return self.name