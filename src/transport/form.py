from django import forms

from .models import user_details

class LoginForm(forms.ModelForm):
    class Meta:
        model = user_details
        fields= [
            "username",
            "password",
        ]