from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label="Enter Username", min_length=4, max_length=50,
                                help_text="Required")
    email = forms.EmailField(max_length=100, help_text="Required",
                             error_messages={"required": "Sorry, you will need an email"})
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ("user_name", 'email',)

##### Form field validations
    def clean_user_name(self):
        user_name = self.cleaned_data["user_name"].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        r = UserBase.objects.filter(email=email)
        if r.count():
            raise forms.ValidationError("Please use another Email, that is already taken")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Username"}
        )
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Email"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat Password"}
        )
