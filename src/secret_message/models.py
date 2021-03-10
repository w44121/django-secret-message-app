from django.db import models
from django.conf import settings


class SecretMessage(models.Model):
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    time_to_destroy = models.PositiveSmallIntegerField()
    amount_to_read = models.PositiveIntegerField(default=1)
