from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'date', 'time', 'people', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'phone', 'date', 'time', 'people')
    list_per_page = 25


admin.site.register(Booking, BookingAdmin)
