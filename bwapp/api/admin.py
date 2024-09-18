from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """Модель продукта для админки."""
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    empty_value_display = '-пусто-'


admin.site.register(Product, ProductAdmin)
