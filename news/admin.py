from django.contrib import admin

from news.models import CategoryNews, News

admin.site.register(CategoryNews)
admin.site.register(News)
