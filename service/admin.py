from django.contrib import admin

from service.models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', 'description']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'stack', 'category']
    search_fields = ['stack', 'name', 'category__name']

