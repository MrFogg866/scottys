from django.urls import path
from . import views

urlpatterns = [
    path('social_media/', views.social_media, name='social_media'),
]