from django.urls import path
from .views import event_book

urlpatterns = [
    path('events/', event_book, name='event_book'),
]
