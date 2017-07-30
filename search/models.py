from __future__ import unicode_literals

from django.db import models

class BerkeleyClass(models.Model):
    # Required fields
    display_name = models.CharField(max_length=10000, unique=True)
    term = models.IntegerField(default=0)
    term_name = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=200, default='')
    number = models.IntegerField(default=0)
    offering_number = models.IntegerField()
    description = models.TextField(max_length=5000, default='')
    subject_code = models.CharField(max_length=100, default='')
    subject = models.CharField(max_length=100, default='')
    enrolled_count = models.IntegerField(default=0)
    waitlisted_count = models.IntegerField(default=0)
    min_enroll = models.IntegerField(default=0)
    max_enroll = models.IntegerField(default=0)
    max_waitlist = models.IntegerField(default=0)
    component_code = models.CharField(max_length=100, default='')
    component = models.CharField(max_length=100, default='')

    # Optional fields
    enrollment_status_code = models.CharField(max_length=100, default='', null=True)
    enrollment_status = models.CharField(max_length=100, default='', null=True)
