from django.contrib import admin
from .models import (Holidays_Packages_Upload,Domestic_Holiday_Package,Central_Asia_Packages,
                    Europe_Packages,Middle_East_Packages,SouthEast_Asia_Packages,Flight_Booking,Hotel_Booking,
                    Visa_Enquiry,
                    Transport_Services
                    )


class Transport_ServicesAdmin(admin.ModelAdmin):
    list_display = [
                    'Full_Name',
                    'Phone',
                    'Email',
                    'Journey_By',
                    'Departure',

                   ]



class Visa_EnquiryAdmin(admin.ModelAdmin):
    list_display = [
                    'Full_Name',
                    'Phone',
                    'Email',
                    'Country',
                    'Duration',

                    ]


class Hotel_BookingAdmin(admin.ModelAdmin):
    list_display = [
                    'Name',
                    'Phone',
                    'Email',
                    'Destination',
                    'Check_In',
                    'Check_Out',
                    'Class',
                    'Adults',
                    'Children',
                    'Rooms',
                    ]


class Flight_BookingAdmin(admin.ModelAdmin):
    list_display = [
                    'Name',
                    'Phone',
                    'From',
                    'To',
                    'Date',
                    'Till_Date',
                    'Class',
                    'Adults',
                    'Children',
                    ]
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
                    'id',
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',
                    'uploaded_at',
                    ]


admin.site.register(Transport_Services,Transport_ServicesAdmin)
admin.site.register(Visa_Enquiry,Visa_EnquiryAdmin)
admin.site.register(Hotel_Booking,Hotel_BookingAdmin)
admin.site.register(Flight_Booking,Flight_BookingAdmin)
admin.site.register(SouthEast_Asia_Packages,SouthEast_Asia_PackagesAdmin)
admin.site.register(Middle_East_Packages,Middle_East_PackagesAdmin)
admin.site.register(Europe_Packages,Europe_PackagesAdmin)
admin.site.register(Central_Asia_Packages,Central_Asia_PackagesAdmin)
admin.site.register(Domestic_Holiday_Package,Domestic_Holiday_PackageAdmin)
admin.site.register(Holidays_Packages_Upload,Holidays_Packages_UploadAdmin)