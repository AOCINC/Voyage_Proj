from django import forms
from .models import Holidays_Packages_Upload,Flight_Booking


class Holidays_Packages_Form(forms.ModelForm):
    class Meta:
        model   =  Holidays_Packages_Upload
        fields  = [
            
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Package',
                    'Location_Image',


                   ]
                
            
class Flight_Booking_Form(forms.ModelForm):
    class Meta:
        model = Flight_Booking
        fields = '__all__'
        widgets = {
                    'Name': forms.TextInput(attrs = {'placeholder':'Your Name'}),
                    'Phone': forms.TextInput(attrs = {'placeholder':'Phone Number'}),
                    'From': forms.TextInput(attrs = {'placeholder':'From'}),
                    'To'  : forms.TextInput(attrs = {'placeholder':'To'}),
                    'Date': forms.TextInput(attrs = {'type':'date'}),
                    'Till_Date': forms.TextInput(attrs = {'type':'date'}),
                    # 'Class':forms.TextInput(attrs = {'placeholder':'Class'})

                   }
