from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


def __str__(self):
    return self.title


class Comment(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
