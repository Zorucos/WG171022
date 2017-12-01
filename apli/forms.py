from django import forms
from .models import Person

YEARS = [x for x in range(1980,2031)]

class PersonForm(forms.ModelForm):
    birthday = forms.DateField(initial="2010-11-20", widget=forms.SelectDateWidget(years=YEARS))
    name = forms.CharField(initial="", label="Person Name")
    comment = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 22}))
    class Meta:
        model=Person
        fields= ['name',
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
        #exclude =[]
        def __init__(self, *args, **kwargs):
            super(PersonForm, self).__init__(*args, **kwargs)
            

        def clean_name(self, *args, **kwargs):
            name = self.cleaned_data.get("name")
            if len(name) < 10:
                raise forms.ValidationError("nope")
            return name
            

# class PersonForm(forms.ModelForm):
#     class Meta: 
#         model = PersonForm
#         fields = [
#             'name',
#             'client',
#             'name_short',
#             'company',
#             'company_short',
#             'country',
#             'city',
#             'zip_code',
#             'address',
#             'email',
#             'phone',
#             'comment',
#             'birthday',
#             'agent',
#             'model',
#             'photographe',
#             'make_up',
#             'styling',
#             'other',
#             'comment_other',
#             'sedcard_cost',
#             'bank_account',
#             'website',
#         ]