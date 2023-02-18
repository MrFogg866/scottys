from .models import Subscriber

from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Subscriber, SubscriberAdmin)
