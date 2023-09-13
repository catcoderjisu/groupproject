from django.db import models

# Create your models here.


class Post(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


def __str__(self):
    return self.title
