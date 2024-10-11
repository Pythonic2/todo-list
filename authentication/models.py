from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)


    def __str__(self):
        return self.username