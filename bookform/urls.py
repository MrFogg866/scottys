from django.urls import path
from .views import book_form, booking_thankyou

urlpatterns = [
    path('', book_form, name='bookform'),
    path('thankyou/', booking_thankyou, name='booking_thankyou'),
]
