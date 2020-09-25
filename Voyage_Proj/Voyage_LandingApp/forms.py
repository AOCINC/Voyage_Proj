from django import forms
from .models import Enquiry_Tab



class Enquiry_Form(forms.ModelForm):
    class Meta:
        model  = Enquiry_Tab
        fields = '__all__'
        widgets = {
                    'Full_Name'     : forms.TextInput(attrs={'placeholder': 'FullName'}),
                    'Email'         : forms.TextInput(attrs={'placeholder': 'Email'}),
                    'Phone'         : forms.TextInput(attrs={'placeholder': 'Phone'}),
                    'Journey_Date'  : forms.TextInput(attrs = {'type': 'date'}),
                    'Destination'   : forms.TextInput(attrs={'placeholder': 'Destination'}),
                    # 'Adults'        : forms.TextInput(attrs={'placeholder': 'People'}),

                    }


