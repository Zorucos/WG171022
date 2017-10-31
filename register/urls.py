from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
# from register.views import (RegisterView)

urlpatterns = [
	#url log in out register
	url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
	url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
	# url(r'^register/$', RegisterView.as_view(template_name='register.html'), name="register"),

	#url para resset password
	url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
	url(r'^admin/password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	]