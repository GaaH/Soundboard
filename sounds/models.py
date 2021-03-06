from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models


class Soundbox(models.Model):
    class Meta:
        verbose_name_plural = 'Soundboxes'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.user, self.title)

    def get_absolute_url(self):
        return reverse('sounds:detail-box', args=(self.pk,))

class Sound(models.Model):
    soundbox = models.ForeignKey(Soundbox, on_delete=models.CASCADE)
    file = models.FileField(upload_to='sounds')
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('sounds:detail', args=(self.pk,))
