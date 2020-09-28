from django import forms
from .models import Holidays_Packages_Upload


class Holidays_Packages_Form(forms.ModelForm):
    class Meta:
        model   =  Holidays_Packages_Upload
        fields  = [
            
                    'Trip_Name',
                    'Days',
                    'Nights',
                    'Datailed_Itinerary',
                    'Location_Image',

                   ]