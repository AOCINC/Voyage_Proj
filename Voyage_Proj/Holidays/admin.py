from django.contrib import admin
from .models import Holidays_Packages_Upload

class Holidays_Packages_UploadAdmin(admin.ModelAdmin):
    list_display = [
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Location_Image',
                    'uploaded_at',
                    ]

    
admin.site.register(Holidays_Packages_Upload,Holidays_Packages_UploadAdmin)