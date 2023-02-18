from django.urls import path
from .views import SignupView

urlpatterns = [
    # other urls
    path('signup/', SignupView.as_view(), name='signup'),
]
