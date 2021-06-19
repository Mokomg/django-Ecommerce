from django import forms
from .models import UserBase
from django.utils.translation import gettext_lazy as _

class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(_("User name"), label="Enter Username", min_length=4, max_length=50,
                                help_text="Required")
    email = forms.EmailField(_("Email"), max_length=100, help_text="Required",
                             error_messages={"required": "Sorry, you will need an email"})
    password = forms.CharField(_("Password"), label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(_("Repeat Password"), label="Repeat Password", widget=forms.PasswordInput)


    class Meta:
        model = UserBase
        fields = ("user_name", 'email',)
