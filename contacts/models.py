from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(
        max_length=255)

    last_name = models.CharField(
        max_length=255)

    email = models.EmailField()
    message = models.TextField()

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])
