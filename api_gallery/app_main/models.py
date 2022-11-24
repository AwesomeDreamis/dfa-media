from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users_images/', null=True, max_length=255)
