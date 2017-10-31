from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import get_user_model #registration

User = get_user_model()




# forma registro nuevo cliente ABRE
class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

        def clean_email(self):
            email = self.cleaned_data.get("email")
            qs = User.objects.filter(email__iexact=email)
            if qs.exists():
                raise forms.ValidationError("Cannot use this email. its all ready register.")
            return email