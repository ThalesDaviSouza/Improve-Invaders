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
