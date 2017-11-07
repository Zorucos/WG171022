from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from django.views.generic import CreateView # registration
from django.contrib.auth import get_user_model #registration
from .forms import RegisterForm, SignUpForm

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate
# from django.contrib.sites.shortcuts import get_current_site
# from django.shortcuts import render, redirect
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string
# from mysite.core.forms import SignUpForm
# from mysite.core.tokens import account_activation_token


User = get_user_model()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = "/register/login"

    


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your MySite Account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
