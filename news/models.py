# coding: utf-8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class CategoryNews(models.Model):
    name_categ = models.CharField(max_length=100, verbose_name="Категория")
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        db_table = "CategoryNews"
        verbose_name_plural = "Категория новостей"

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.name_categ


class News(models.Model):
    title_news = models.CharField(max_length=255, verbose_name="Заголовок")
    photo_news = models.ImageField(upload_to="news/", verbose_name="Фото")
    description_news = models.TextField(verbose_name="Описание")
    data_pub = models.DateField(verbose_name="Дата публикации", auto_now=True)
    category_news = models.ForeignKey(CategoryNews, verbose_name="Категория", related_name='default_category',
                                      null=True, blank=True)
    categories = models.ManyToManyField('CategoryNews', blank=True)

    class Meta:
        db_table = "News"
        verbose_name_plural = "Новости"

    # def get_absolute_url(self):
    #     return reverse()

    def __unicode__(self):
        return self.title_news
