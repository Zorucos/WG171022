from django.contrib.auth.models import User
from django import forms
from .models import Person, Project, Attachment, Assignment, Horaire, Cost, Time



class Person(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
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
        ]