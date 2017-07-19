from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models


class Sound(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='sounds')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('sounds:detail', args=[self.pk])
