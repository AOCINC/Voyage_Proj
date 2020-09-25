from django.contrib import admin
from .models import Enquiry_Tab

class Enquiry_Admin(admin.ModelAdmin):
    list_display = [
                    'Full_Name',
                    'Email',
                    'Phone',
                    'Journey_Date',
                    'Destination',
                    'Adults',
                     ]




                     
admin.site.register(Enquiry_Tab, Enquiry_Admin)