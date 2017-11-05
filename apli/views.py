# Python first
# django second
# your apps
# local directory


from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required # requisito login  def
from django.contrib.auth.mixins import LoginRequiredMixin # requisito login  viw 
from django.views.generic import View
from .models import Person, Project, Attachment, Assignment, Horaire, Cost, Time
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
# para mandar email
from django.core.mail import send_mail # send email
from django.contrib import messages 
from django.conf import settings # mail


# DASHBOARD 

@login_required(login_url='/register/login/')
def dashboard(request):
    return render(request, 'apli/menu/dashboard/dashboard.html', )

# PERSON: index, detail, create, update, delete.

@login_required(login_url='/register/login/')
def person_index(request):
    all_persons = Person.objects.all()
    return render(request, 'apli/menu/person/person_index.html', {'all_persons': all_persons})

@login_required(login_url='/register/login/')
def person_detail(request, pk):
    person = get_object_or_404(Person, id=pk)
    all_projects = person.project_set.all()
    return render(request, 'apli/menu/person/person_detail.html', {'person': person, 'all_projects': all_projects})


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['name', 'name_short', 'company', 'company_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone', 'comment']

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['name', 'name_short', 'company', 'company_short', 'agent', 'agent_short', 'country', 'city', 'zip_code', 'address', 'email', 'phone','email','sedcard','statut','comment','bank_account', 'website']


class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('index_person')   

#  PROJECT
@login_required(login_url='/register/login/')
def project_index(request):
    all_projects = Project.objects.all()
    return render(request, 'apli/menu/project/project_index.html', {'all_projects': all_projects})
    
@login_required(login_url='/register/login/')   
def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    all_persons = project.assignment_set.all()
    all_attachments = project.attachment_set.all()
    all_costs = project.cost_set.all()
    return render(request, 'apli/menu/project/project_detail.html', {'project': project, 'all_persons': all_persons, 'all_attachments': all_attachments, 'all_costs': all_costs})