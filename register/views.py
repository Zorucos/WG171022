from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from django.views.generic import CreateView # registration
from django.contrib.auth import get_user_model #registration
from .forms import RegisterForm

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate



User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/register/login"

    
#     def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
