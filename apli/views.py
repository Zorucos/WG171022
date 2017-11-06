# Python first
# django second
# your apps
# local directory


from django.shortcuts import render, get_object_or_404, redirect
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

#--------------------------
# INDICE (ordenar alfabéticamente)
# 1- dashboard ...linea 28
# 2- PERSON    ...linea 34
# 3- Project   ...linea 107
# -------------------------


@login_required(login_url='/register/login/')
def assignment_index(request):
    all_assignments = Assignment.objects.all().filter(sort='')
    return render(request, 'apli/menu/assignment/assignments_index.html', {'all_assignments': all_assignments})

@login_required(login_url='/register/login/')
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, id=pk)
    all_horaire = assignment.horaire_set.all()
    return render(request, 'apli/menu/assignment/assignment_detail.html', {'assignment': assignment, 'all_horaire': all_horaire})

class AssignmentCreate(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = ['project',
            'person',
            'model_type',
            'travel_cost',
            'hotel_cost',
            'other_cost',
            'comment_WG',
            'statut',
            'send_date',
            'payment_date',
            'total_price'
            ]

class AssignmentUpdate(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = ['project',
            'person',
            'model_type',
            'travel_cost',
            'hotel_cost',
            'other_cost',
            'comment_WG',
            'statut',
            'send_date',
            'payment_date',
            'total_price'
            ]


class AssignmentDelete(LoginRequiredMixin, DeleteView):
    model = Assignment
    success_url = reverse_lazy('assignment_index')


# 1- DASHBOARD 

@login_required(login_url='/register/login/')
def dashboard(request):
    return render(request, 'apli/menu/dashboard/dashboard.html', )

# 2- PERSON: index, detail, create, update, delete.

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
    fields = ['name',
            'name_short',
            'company',
            'company_short',
            'country',
            'city',
            'zip_code',
            'address',
            'email',
            'phone',
            'comment',
            'birthday',
            'agent',
            'client',
            'model',
            'photographe',
            'make_up',
            'styling',
            'other',
            'comment_other',
            'sedcard_cost',
            'bank_account',
            'website'
            ]

class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['name',
            'name_short',
            'company',
            'company_short',
            'country',
            'city',
            'zip_code',
            'address',
            'email',
            'phone',
            'comment',
            'birthday',
            'agent',
            'client',
            'model',
            'photographe',
            'make_up',
            'styling',
            'other',
            'comment_other',
            'sedcard_cost',
            'bank_account',
            'website'
            ]

class PersonDelete(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person_index')   


#  PROJECT: Index, detail, create, update, delete.

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

class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['name',
            'client',
            'start',
            'finish',
            'user',
            'comment',
            'sort',
            'all_day',
            'half_day',
            'half_day_price_pro',
            'all_day_price_pro',
            'over_price_pro',
            'all_in_price_pro',
            'half_day_price_semipro',
            'all_day_price_semipro',
            'over_price_semipro',
            'all_in_price_semipro',
            'country',
            'city',
            'zip_code',
            'address',
            'comment_address',
            'honorary_base',
            'honorary_plus',
            'quantity_models_honorary_plus',
            'ms_price',
            'ms_hours',
            'requirement_price',
            'requirement_hours',
            'requisiten_price_for_each_model',
            'other_title',
            'other_description',
            'other_price',
            'other_hours',
            'photo_price',
            'photo_hours',
            'tax',
            ]


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['name', 'client', 'start', 'finish', 'user', 'comment', 'sort', 'all_day', 'half_day', 'half_day_price_pro', 'all_day_price_pro', 'over_price_pro', 'all_in_price_pro', 'half_day_price_semipro', 'all_day_price_semipro', 'over_price_semipro', 'all_in_price_semipro', 'country', 'city', 'zip_code', 'address', 'comment_address', 'honorary_base', 'honorary_plus', 'quantity_models_honorary_plus', 'ms_price', 'ms_hours', 'requirement_price', 'requirement_hours', 'requisiten_price_for_each_model', 'other_title', 'other_description', 'other_price', 'other_hours', 'photo_price', 'photo_hours', 'tax']


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project_index')