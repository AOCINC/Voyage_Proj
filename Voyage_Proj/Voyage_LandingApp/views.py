from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Enquiry_Tab
from Holidays.models import(Holidays_Packages_Upload,Domestic_Holiday_Package,Central_Asia_Packages,   
                            Europe_Packages,
                            Middle_East_Packages,
                            SouthEast_Asia_Packages,
                            ) #importing holidays app models for counting the packages 
from .forms import Enquiry_Form
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Context
import wikipedia
import requests






def home_view(request):
    Domestic_count    = Domestic_Holiday_Package.objects.all().count()
    CentralAsia_Count = Central_Asia_Packages.objects.all().count()
    Europe_count      = Europe_Packages.objects.all().count()
    MiddleEast_count  = Middle_East_Packages.objects.all().count()
    SouthEast_Asia_count = SouthEast_Asia_Packages.objects.all().count()
    template_name = 'Voyage_LandingApp/home.html'
    context    = {
                 'Domestic_count':Domestic_count,
                 'CentralAsia_Count':CentralAsia_Count,
                 'Europe_count':Europe_count,
                 'MiddleEast_count':MiddleEast_count,
                 'SouthEast_Asia_count':SouthEast_Asia_count,
                 }
    return render(request,template_name,context)

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



def Contact_View(request):
    if request.method == 'POST':
        firstname = request.POST['firstName']
        lastname  = request.POST['lastName']
        email     = request.POST['email']
        phone     = request.POST['phone']
        msg       = request.POST['message']
        subject        = 'Some One Contacted You From voyage Holidayz'
        context        = {
                            'firstname':firstname,
                            'lastname':lastname,
                            'email':email,
                            'phone':phone,
                            'msg':msg,
                            }
        voyage_email    = 'aocincpvtltd@gmail.com'
        from_email      = voyage_email
        to              =[voyage_email,]
        message         = get_template('Voyage_LandingApp/Contact_email.html').render(context)
        msg             = EmailMessage(subject,message,to=to,from_email=from_email,)
        msg.content_subtype = 'html'
        msg.send()
        return redirect('home')
    template = 'Voyage_LandingApp/Contact_View.html'
    return render(request,template)


# about us page 
def AboutUs_View(request):
    template = 'Voyage_LandingApp/AboutUs.html'
    return render(request,template)


# def search_places_wiki_veiw(request):
#     '''if end user search any thing in search box it will fetched the data from wikipedia '''


#     template = 'Voyage_LandingApp/Search_wiki.html'
#     if request.method == 'POST':
#         search_name = request.POST['wiki_name']
#         try:
#             search = wikipedia.page(search_name)
#         except wikipedia.exceptions.DisambiguationError as e:
#             print(e)
#         page_Data = search.summary
#         fomatted_data = page_Data.split('.')
#         all_images = search.images
#         new_images = []
#         for image in all_images:
#             if image.endswith('.jpg') or image.endswith('.png') or image.endswith('.jpeg'):
#                 new_images.append(image)   
#             else:
#                 print('not jpg image==================>')
                
#         context  = {
#                     'search':search,
#                     'new_images':new_images,
#                     # 'all_images':all_images,
#                     'fomatted_data':fomatted_data,
#                     }
#     return render(request, template,context)

def search_places_wiki_veiw(request):
    '''if end user search any thing in search box it will fetched the data from wikipedia '''
    template = 'Voyage_LandingApp/Search_wiki.html'
    options = None
    new_images = []
    fomatted_data = None
    page_id = None
    connection_Err = None
    if request.method == 'POST':
        search_name = request.POST['wiki_name']
        wiki_name   = search_name.strip()
        try:
            searched_Data = wikipedia.page(wiki_name,auto_suggest=False,redirect=True)
            page_Data     = searched_Data.summary
            fomatted_data = page_Data.split('.')
            all_images = searched_Data.images
            for image in all_images:
                if image.endswith('.jpg') or image.endswith('.png') or image.endswith('.jpeg'):
                    new_images.append(image)   
                else:
                    print('===============> not jpg,png,jpeg image..')
        except wikipedia.exceptions.PageError as e:
            page_id = e
        except requests.exceptions.ConnectionError as e:
            connection_Err = e
            print(connection_Err)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options
    context = {
                'options':options,
                'new_images':new_images,
                'fomatted_data':fomatted_data,
                'page_id':page_id,
              } 
    return render(request, template,context)


# exception for timeout
# requests.exceptions.ConnectionError:
# requests.exceptions.ConnectionError: HTTPConnectionPool