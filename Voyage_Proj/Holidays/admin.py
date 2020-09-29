from django.contrib import admin
from .models import (Holidays_Packages_Upload,Domestic_Holiday_Package,Central_Asia_Packages,
                    Europe_Packages,Middle_East_Packages,SouthEast_Asia_Packages,
                    )

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

class Central_Asia_PackagesAdmin(admin.ModelAdmin):
    list_display = [
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',
                    'uploaded_at',
                    ]

class Europe_PackagesAdmin(admin.ModelAdmin):
    list_display = [
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',
                    'uploaded_at',
                    ]

class Middle_East_PackagesAdmin(admin.ModelAdmin):
    list_display = [
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',
                    'uploaded_at',
                    ]

class SouthEast_Asia_PackagesAdmin(admin.ModelAdmin):
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


admin.site.register(SouthEast_Asia_Packages,SouthEast_Asia_PackagesAdmin)
admin.site.register(Middle_East_Packages,Middle_East_PackagesAdmin)
admin.site.register(Europe_Packages,Europe_PackagesAdmin)
admin.site.register(Central_Asia_Packages,Central_Asia_PackagesAdmin)
admin.site.register(Domestic_Holiday_Package,Domestic_Holiday_PackageAdmin)
admin.site.register(Holidays_Packages_Upload,Holidays_Packages_UploadAdmin)