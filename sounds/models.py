from django.contrib.auth.models import User
from django.db import models


class Sound(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='sounds')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
