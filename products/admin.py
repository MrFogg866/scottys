from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',

    )

    ordering =('sku',)

class CatergoryAdmin(admin.ModelAdmin):
    list_display = (
        'freindly_name',
        'name',
    )


admin.site.register(Product)
admin.site.register(Category)