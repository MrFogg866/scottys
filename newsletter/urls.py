# urls.py
from django.urls import path
from newsletter.views import subscribe, thank_you

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('thank-you/', thank_you, name='thank_you'),
]
