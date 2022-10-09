from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.CharField(
        max_length=10,
        choices=[("ESTUDANTE", "Estudante"), ("PROFESSOR", "Professor")],
        blank=True,
        null=True)


    def __str__(self):
        return self.user.username


class Sala(models.Model):
    professor = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name 

class Task(models.Model):
    sala = models.OneToOneField(Sala, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class StudentWork(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task")
    content = models.TextField()
    status = models.CharField(
        max_length=12,
        choices=[("PENDENTE", "Pendente"), ("ENVIADA", "Enviada")])
    
    def __str__(self):
        return f"{self.user.username}, {self.task.name}"

