from django.urls import path
from Holidays import views

urlpatterns = [
    path('Holidays-Packages-Upload',views.Holidays_PackagesUpload_View, name = 'Holidays_Packages_Packages'),
    path('Holidays-Packages',views.Holidays_Packages_List_View, name = 'Holidays_Packages'),
    path('Domestic-Packages',views.Domestic_Holiday_Package_List_View, name = 'Domestic_Packages'),
]

