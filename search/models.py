from __future__ import unicode_literals

from django.db import models

class BerkeleyClass(models.Model):
    # Required fields
    display_name = models.CharField(max_length=10000, unique=True)
    term = models.IntegerField()
    term_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    offering_number = models.IntegerField()
    description = models.TextField(max_length=5000)
    subject_code = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    enrolled_count = models.IntegerField()
    waitlisted_count = models.IntegerField()
    min_enroll = models.IntegerField()
    max_enroll = models.IntegerField()
    max_waitlist = models.IntegerField()

    # Optional fields
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    enrollment_status_code = models.CharField(max_length=100, default='', null=True)
    enrollment_status = models.CharField(max_length=100, default='', null=True)
