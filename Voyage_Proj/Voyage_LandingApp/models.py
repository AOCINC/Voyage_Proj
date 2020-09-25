from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings


class Enquiry_Tab(models.Model):
    Full_Name      = models.CharField(max_length=129)
    Email          = models.EmailField(max_length=159)
    Phone          = models.CharField(max_length=12,validators = [RegexValidator(r'^\d{1,12}$')], default = '')
    Journey_Date   = models.DateField(default = '')
    Destination    = models.CharField(max_length=129)
    Adults         = models.PositiveIntegerField(default = 0, help_text = 'People')


# Journey_Date