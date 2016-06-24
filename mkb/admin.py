from django.contrib import admin

from mkb.models import ClassMKB

class MKBAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ['name','code']

admin.site.register(ClassMKB, MKBAdmin)