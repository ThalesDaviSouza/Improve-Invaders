from django import forms
from django.forms import ModelForm
from .models import UserType, Sala, Task, StudentWork


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

        widgets = {
            'name':forms.TextInput(
                attrs={
                    'class':'icon icon-user-1',
                    'placeholder':'Nome da sala'
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'class':'icon icon-comments',
                    'placeholder':'Descrição da sala'
                }
            )
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
            'name':forms.TextInput(
                attrs={
                    'class':'icon icon-user-1',
                    'placeholder':'Nome da tarefa'
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'class':'icon icon-comments',
                    'placeholder':'Descrição da tarefa'
                }
            ),
            'dataEntrega':forms.DateInput(
                format=('%d-%m-%Y'),
                attrs={
                    'class':'form-control',
                    'type':'date'                    
                }
            ),
        }


class StudentWorkForm(ModelForm):
    class Meta:
        model = StudentWork
        fields = ['content']

        labels = {
            'content': 'Sua tarefa feita',
        }

        
        widgets = {
            'content':forms.Textarea(
                attrs={
                    'class':'icon icon-comments',
                    'placeholder':'Sua atividade vai aqui...'
                }
            )
        }