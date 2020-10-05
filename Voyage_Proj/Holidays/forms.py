from django import forms
from .models import Holidays_Packages_Upload,Flight_Booking,Hotel_Booking,Visa_Enquiry,Transports_Enquiry


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
                    'Email': forms.TextInput(attrs = {'placeholder':'Email'}),
                    'From': forms.TextInput(attrs = {'placeholder':'From'}),
                    'To'  : forms.TextInput(attrs = {'placeholder':'To'}),
                    'Date': forms.TextInput(attrs = {'type':'date'}),
                    'Till_Date': forms.TextInput(attrs = {'type':'date'}),
                    # 'Class':forms.TextInput(attrs = {'placeholder':'Class'})

                   }

class Hotel_Booking_Form(forms.ModelForm):
    class Meta:
        model = Hotel_Booking
        fields = '__all__'
        widgets = {
                    'Name':forms.TextInput(attrs = {'placeholder':'Your Name'}),
                    'Phone': forms.TextInput(attrs = {'placeholder':'Phone Number'}),
                    'Email': forms.TextInput(attrs = {'placeholder':'Email'}),
                    'Destination':forms.TextInput(attrs = {'placeholder':'Destination '}),
                    'Check_In': forms.TextInput(attrs = {'type':'date'}),
                    'Check_Out': forms.TextInput(attrs = {'type':'date'}),



                  }

class Visa_Enquiry_Form(forms.ModelForm):
    class Meta:
        model  = Visa_Enquiry
        fields = '__all__'
        widgets ={
                  'Full_Name': forms.TextInput(attrs = {'placeholder':'Full Name'}),
                  'Phone'    : forms.TextInput(attrs = {'placeholder':'Phone'}),
                  'Email'    : forms.TextInput(attrs = {'placeholder':'Email'}),
                  'Country'  : forms.TextInput(attrs = {'placeholder':'Country'}),
                #   'Duration' : forms.TextInput(attrs = {'placeholder':'Duration'})

                 }
        
class Transports_Enquiry_Form(forms.ModelForm):
    class Meta:
        model = Transports_Enquiry
        fields = '__all__'
        widgets = {
                    'Full_Name' : forms.TextInput(attrs = {'placeholder':'Full Name'}),
                    'Phone'    : forms.TextInput(attrs = {'placeholder':'Phone'}),
                    'Email'     :  forms.TextInput(attrs = {'placeholder':'Email'}),
                    'Destination': forms.TextInput(attrs = {'placeholder':'Destination'}),
                    'Jouryney_Date': forms.TextInput(attrs = {'type':'date'}),
                    # 'Journey_By': forms.TextInput(attrs = {'type':'date'}),
                  }
