from django.db import models
from django.conf import settings


class SecretMessage(models.Model):
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    time_to_destroy = models.PositiveSmallIntegerField()
    amount_to_read = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.text}, time to destroy: {self.time_to_destroy}"

    @property
    def is_read_limit_over(self):
        return self.amount_to_read < 0
    
    def save(self, *args, **kwargs):
        self.amount_to_read -= 1
        super().save(*args, **kwargs)
