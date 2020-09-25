from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Enquiry_Tab
from .forms import Enquiry_Form
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Context






def home_view(request):
    template_name = 'Voyage_LandingApp/home.html'
    return render(request,template_name)

@login_required
def Enquiry_View(request):
    if request.method == 'POST':
        Form   = Enquiry_Form(request.POST or None)
        if Form.is_valid():
            name        = Form.cleaned_data['Full_Name']
            email       = Form.cleaned_data['Email']
            phone       = Form.cleaned_data['Phone']
            j_Date      = Form.cleaned_data['Journey_Date']
            print(j_Date)
            destination = Form.cleaned_data['Destination']
            people      = Form.cleaned_data['Adults']
            subject     = 'A New Traveller Posted His Details For Package..'
            context     = {
                            'name':name,
                            'email':email,
                            'phone':phone,
                            'j_Date':j_Date,
                            'destination':destination,
                            'people':people,
                          }
            voyage_email = 'aocincpvtltd@gmail.com'
            from_email   = voyage_email
            to           = [voyage_email,]
            message = get_template('Voyage_LandingApp/Enquiry_email.html').render(context)
            msg = EmailMessage(subject, message, to=to,from_email = from_email)
            msg.content_subtype  = 'html'
            msg.send() 
            Form.save()
            messages.success(request,'Done!, We Will Contact You Soon')
            return redirect('home')
    else:
        Form = Enquiry_Form()
    template   = 'Voyage_LandingApp/Enquiry_Form.html'
    context    =  {
                   'Form':Form,
                   }
    return render(request,template,context)



