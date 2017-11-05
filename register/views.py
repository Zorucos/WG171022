from django.shortcuts import render
from django.views.generic import View, CreateView

from django.views.generic import CreateView # registration
from django.contrib.auth import get_user_model #registration
from .forms import RegisterForm




User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/register/login"

