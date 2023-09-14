from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=100)
    content = models.TextField()
    starting_date = models.DateField()
    finishing_date = models.DateField('finishing date', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


def __str__(self):
    return self.title
