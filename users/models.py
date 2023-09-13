from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass


class post(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
