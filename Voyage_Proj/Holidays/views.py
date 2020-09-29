from django.shortcuts import render, redirect
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

