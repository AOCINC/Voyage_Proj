from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import (Holidays_Packages_Upload,Domestic_Holiday_Package,
                    Central_Asia_Packages,Europe_Packages,Middle_East_Packages,
                    SouthEast_Asia_Packages,

                    )
from .forms import Holidays_Packages_Form




def Holidays_PackagesUpload_View(request):
    ''' 
        Agent Will Upload all the Trip/Holiday Package Info From This View.
    '''
    if request.method   == 'POST':
        Form   = Holidays_Packages_Form(request.POST,request.FILES)
        if Form.is_valid():
            tripName    = Form.cleaned_data['Trip_Name']
            days        = Form.cleaned_data['Days']
            nights      = Form.cleaned_data['Nights']
            Itinerary   = Form.cleaned_data['Datailed_Itinerary']
            image       = Form.cleaned_data['Location_Image']
            package     = Form.cleaned_data['Package']
            if package == 'Domestic':
                domestic_tab   = Domestic_Holiday_Package(Trip_Name = tripName, Days = days, Nights = nights, Datailed_Itinerary = Itinerary, Location_Image = image, Package = package)
                domestic_tab.save()
            if package == 'CentralAsia':
                CentralAsia_tab   = Central_Asia_Packages(Trip_Name = tripName, Days = days, Nights = nights, Datailed_Itinerary = Itinerary, Location_Image = image, Package = package)
                CentralAsia_tab.save()
            if package == 'Europe':
                Europe_tab        = Europe_Packages(Trip_Name = tripName, Days = days, Nights = nights, Datailed_Itinerary = Itinerary, Location_Image = image, Package = package)
                Europe_tab.save()
            if package == 'MiddleEast':
                MiddleEast_tab    = Middle_East_Packages(Trip_Name = tripName, Days = days, Nights = nights, Datailed_Itinerary = Itinerary, Location_Image = image, Package = package)
                MiddleEast_tab.save()
            if package == 'SouthEast_Asia':
                SouthEast_Asia_tab  = SouthEast_Asia_Packages(Trip_Name = tripName, Days = days, Nights = nights, Datailed_Itinerary = Itinerary, Location_Image = image, Package = package)
                SouthEast_Asia_tab.save()
            else:
                print('nothing selected...')
            Form.save() # saving the data into holiday packages table to render all packages at one place i.e., Domestic & International
            return redirect('home')
    else:
        Form  = Holidays_Packages_Form()
    template  = 'Holidays/Holidays_Package_Upload.html'
    context   = {
                 'Form':Form,
                }
    return render(request, template,context)



def Holidays_Packages_List_View(request):
    '''
        All The Uploaded Trip/Holiday Packages Info Will List In This View
    '''
    Holiday_Data_list = Holidays_Packages_Upload.objects.all().order_by('-id')
    # paginator...
    paginator = Paginator(Holiday_Data_list, 8)
    page = request.GET.get('page')
    try:
        Data_list = paginator.page(page)
    except PageNotAnInteger:
        Data_list = paginator.page(1)
    except EmptyPage:
        Data_list = paginator.page(paginator.num_pages) 
    template = 'Holidays/Holidays_Packages.html'
    context = {
                'Data_list': Data_list,
                }
    return render(request,template,context)



def All_Holidays_Package_Detail(request, id = None):
    '''all domestic internation package detial view  ''' 
    All_Holidays_Package_Data = get_object_or_404(Holidays_Packages_Upload, id = id) 
    package  = All_Holidays_Package_Data.Package
    context = {
        'All_Holidays_Package_Data':All_Holidays_Package_Data,
    }
    template = 'Holidays/All_Holidays_Package_Detial.html'

    return render(request,template,context)




def Domestic_Holiday_Package_List_View(request):
    '''
        All Domestic Packages  Info Will List In This View
    '''
    Domestic_Data_List = Domestic_Holiday_Package.objects.all().order_by('-id')
    # paginator...
    paginator = Paginator(Domestic_Data_List, 8)
    page = request.GET.get('page')
    try:
        Data_list = paginator.page(page)
    except PageNotAnInteger:
        Data_list = paginator.page(1)
    except EmptyPage:
        Data_list = paginator.page(paginator.num_pages) 

    template = 'Holidays/Domestic_Packages.html'
    context = {
                'Data_list': Data_list,
                }
    return render(request,template,context)



def Domestic_Holiday_Package_Detail(request, id = None):
    Domestic_Holiday_Package_Data = get_object_or_404(Domestic_Holiday_Package, id = id) 
    context = {
        'Domestic_Holiday_Package_Data':Domestic_Holiday_Package_Data,
    }
    template = 'Holidays/Domestic_Package_Detial.html'

    return render(request,template,context)




def Central_Asia_Packages_List_View(request):
    '''
        All central aisa  Packages  Info Will List out In This View
    '''
    CentralAsia_Data_List = Central_Asia_Packages.objects.all().order_by('-id')
    # paginator...
    paginator = Paginator(CentralAsia_Data_List, 8)
    page = request.GET.get('page')
    try:
        Data_list = paginator.page(page)
    except PageNotAnInteger:
        Data_list = paginator.page(1)
    except EmptyPage:
        Data_list = paginator.page(paginator.num_pages) 

    template = 'Holidays/CentralAsia_Packages.html'
    context = {
                'Data_list': Data_list,
                }
    return render(request,template,context)


def Central_Asia_Package_Detail(request, id = None):
    Central_Asia_Package_Data = get_object_or_404(Central_Asia_Packages, id = id) 
    context = {
        'Central_Asia_Package_Data':Central_Asia_Package_Data,
    }
    template = 'Holidays/Central_Asia_Package_Detial.html'

    return render(request,template,context)
    



def Europe_Packages_List_View(request):
    '''
        All Europe Packages  Packages  Info Will List out In This View
    '''
    Europe_Packages_Data_List = Europe_Packages.objects.all().order_by('-id')
    # paginator...
    paginator = Paginator(Europe_Packages_Data_List, 8)
    page = request.GET.get('page')
    try:
        Data_list = paginator.page(page)
    except PageNotAnInteger:
        Data_list = paginator.page(1)
    except EmptyPage:
        Data_list = paginator.page(paginator.num_pages) 

    template = 'Holidays/Europe_Packages.html'
    context = {
                'Data_list': Data_list,
                }
    return render(request,template,context)


def Europe_Package_Detail(request, id = None):
    Europe_Package_Data = get_object_or_404(Europe_Packages, id = id) 
    context = {
        'Europe_Package_Data':Europe_Package_Data,
    }
    template = 'Holidays/Europe_Package_Detial.html'

    return render(request,template,context)




def Middle_East_Packages_List_View(request):
    '''
        All Middle East Packages  Info Will List out In This View
    '''
    Middle_East_Packages_Data_List = Middle_East_Packages.objects.all().order_by('-id')
    # paginator...
    paginator = Paginator(Middle_East_Packages_Data_List, 8)
    page = request.GET.get('page')
    try:
        Data_list = paginator.page(page)
    except PageNotAnInteger:
        Data_list = paginator.page(1)
    except EmptyPage:
        Data_list = paginator.page(paginator.num_pages) 

    template = 'Holidays/MiddleEast_Packages.html'
    context = {
                'Data_list': Data_list,
                }
    return render(request,template,context)


def MiddleEast_Package_Detail(request, id = None):
    MiddleEast_Data = get_object_or_404(Middle_East_Packages, id = id) 
    context = {
        'MiddleEast_Data':MiddleEast_Data,
    }
    template = 'Holidays/MiddleEast_Package_Detial.html'

    return render(request,template,context)





def SouthEast_Asia_Packages_List_View(request):
    '''
        All SouthEast Asia Packages  Info Will List out In This View
    '''
    SouthEast_Asia_Packages_Data_List = SouthEast_Asia_Packages.objects.all().order_by('-id')
    # paginator...
    paginator = Paginator(SouthEast_Asia_Packages_Data_List, 8)
    page = request.GET.get('page')
    try:
        Data_list = paginator.page(page)
    except PageNotAnInteger:
        Data_list = paginator.page(1)
    except EmptyPage:
        Data_list = paginator.page(paginator.num_pages) 

    template = 'Holidays/SouthEast_Asia_Packages.html'
    context = {
                'Data_list': Data_list,
                }
    return render(request,template,context)

def SouthEast_Asia_Packages_Detail(request, id = None):
    SouthEast_Asia_Packages_Data = get_object_or_404(SouthEast_Asia_Packages, id = id) 
    context = {
        'SouthEast_Asia_Packages_Data':SouthEast_Asia_Packages_Data,
    }
    template = 'Holidays/SouthEast_Asia_Package_Detial.html'

    return render(request,template,context)