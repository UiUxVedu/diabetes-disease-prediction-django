from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# --------------------
# REGISTRATION FORM
# --------------------
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


# --------------------
# LOGIN FORM
# --------------------
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
