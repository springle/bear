from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
