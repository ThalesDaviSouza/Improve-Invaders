from django import forms
from django.forms import ModelForm
from .models import UserType, Sala, Task


class UserTypeForm(ModelForm):
    class Meta:
        model = UserType
        fields = ['userType']

        labels = {
            'userType': 'Você é:',
        }
        


class SalaForm(ModelForm):
    class Meta:
        model = Sala
        fields = ['name', 'description']

        labels = {
            'name': 'Nome da Sala',
            'description': 'Descrição'
        }


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'dataEntrega']

        labels = {
            'name': 'Nome da tarefa',
            'description': 'Descrição',
            'dataEntrega': 'Data de entrega',
        }

        widgets = {
            'dataEntrega':forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'class':'form-control',
                    'type':'date'                    
                }
            ),
        }



