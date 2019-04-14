from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f'Welcome, {self.user.username}'


class Remedies(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    precaution = models.TextField()
    disease_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='fertilizers')

    def __str__(self):
        return f'Welcome, {self.user.username}'

