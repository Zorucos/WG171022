from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from register.views import RegisterView
from . import views
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete



urlpatterns = [


	# LOGIN / OUT
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
	url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),

	# REGISTER
	url(r'^register/$', RegisterView.as_view(template_name='register.html'), name="register"),
# 	url(r'^signup/$', register_views.signup, name='signup'),


	# RESET PASSWORD
	url(r'^reset-password/$', auth_views.password_reset, name='password_reset'),
	url(r'^reset-password/done$', auth_views.password_reset_done, name='password_reset_done'),
	url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
	url(r'^reset-password/complete$', auth_views.password_reset_complete, name='password_reset_complete')
	#url('^', include('django.contrib.auth.urls')), #este url, incluye todo lo anteriormente expuesto. 
	]
