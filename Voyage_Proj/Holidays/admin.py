from django.contrib import admin
from .models import Holidays_Packages_Upload,Domestic_Holiday_Package

class Holidays_Packages_UploadAdmin(admin.ModelAdmin):
    list_display = [
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',
                    'uploaded_at',
                    ]

class Domestic_Holiday_PackageAdmin(admin.ModelAdmin):
    list_display = [
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',
                    'uploaded_at',
                    ]


admin.site.register(Domestic_Holiday_Package,Domestic_Holiday_PackageAdmin)
admin.site.register(Holidays_Packages_Upload,Holidays_Packages_UploadAdmin)