from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userType = models.CharField(
        max_length=10,
        choices=[("ESTUDANTE", "Estudante"), 
            ("PROFESSOR", "Professor")],
        blank=True,
        null=True)


    def __str__(self):
        return self.user.username


class Sala(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name 


class Task(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    dataUpload = models.DateField(null=True)
    dataEntrega = models.DateField(null=True)

    def __str__(self):
        return self.name


class StudentWork(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.CharField(
        max_length=12,
        choices=[("PENDENTE", "Pendente"), ("ENVIADA", "Enviada")])
    
    def __str__(self):
        return f"{self.user.username}, {self.task.name}"

class EnrolledCourses(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Sala, blank=True, related_name='Alunos')

    def __str__(self):
        return f"{self.student.username} courses"