from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('id' , 'name')
    search_help_text = 'Поиск по айди и названию'

""" Регистрируем модель """
admin.site.register(Category, CategoryAdmin)