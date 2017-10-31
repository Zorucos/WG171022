from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required #login  def
from django.contrib.auth.mixins import LoginRequiredMixin #login  viw 
from django.views.generic import CreateView # registration
from django.contrib.auth import get_user_model #registration
from .forms import RegisterForm


User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'apli/register.html'
    success_url = "/apli/index_contact"