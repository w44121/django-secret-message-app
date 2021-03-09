from django.db import models
from django.conf import settings


class SecrteMessage(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    time_to_destroy = models.TimeField()
