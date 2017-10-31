from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # requisito login  def
from django.contrib.auth.mixins import LoginRequiredMixin # requisito login  viw 


# Create your views here.
# @login_required(login_url='/register/login/')
def dashboard(request):
    return render(request, 'apli/menu/dashboard/dashboard.html', )