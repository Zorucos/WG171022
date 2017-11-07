from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import get_user_model #registration

User = get_user_model()


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name    = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name     = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email         = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date    = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )





# forma registro nuevo cliente ABRE
class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email') 
        # , 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Cannot use this email. its all ready register.")
        return email 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        #user.is_staff = False
        # create a new user hash for activating email.

        if commit:
            user.save()
           
            # user.send_activation_email(self)
        return user
