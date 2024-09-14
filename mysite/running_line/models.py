from django.conf import settings
from django.db import models


class Request(models.Model):
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text