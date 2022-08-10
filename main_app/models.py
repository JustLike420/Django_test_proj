from django.db import models


# Create your models here.

class PoliceCalls(models.Model):
    crime_id = models.IntegerField()
    original_crime_type_name = models.CharField(max_length=255)
    report_date = models.DateTimeField()
    call_date = models.DateTimeField()
    offense_date = models.DateTimeField()
    call_time = models.TimeField()
    call_date_time = models.DateTimeField()
    disposition = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255)
    common_location = models.CharField(max_length=255)
