from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('review/', views.create_review, name='create_review'),
    path('review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
