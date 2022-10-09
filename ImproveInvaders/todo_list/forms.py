from django import forms
from django.forms import ModelForm
from .models import UserType


class UserTypeForm(ModelForm):
    class Meta:
        model = UserType
        fields = ['userType']

        labels = {
            'userType': 'Você é:',
        }
        

        