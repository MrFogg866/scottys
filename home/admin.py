from django.contrib import admin
from .models import Review, Subscriber


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'comment', 'related_products')

    def related_products(self, obj):
        return ", ".join([p.name for p in obj.products.all()])

    related_products.short_description = 'Related Products'


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
