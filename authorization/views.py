from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from authorization.forms import LoginForm
from django.contrib.auth import logout


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authorization/signup.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'authorization/login.html'


def logout_view(request):
    logout(request)
    return redirect('login')
