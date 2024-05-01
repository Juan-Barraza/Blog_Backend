from django.contrib.auth.models import AbstractUser
from django.db import models
from blog.managers import UserManager


class User(AbstractUser, models.Model):
    username = models.CharField(('Nombre de usuario'),max_length=255)
    email = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=20)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"
    
    