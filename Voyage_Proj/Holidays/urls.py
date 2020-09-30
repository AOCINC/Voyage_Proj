from django.urls import path
from Holidays import views

urlpatterns = [
    path('Holidays-Packages-Upload',views.Holidays_PackagesUpload_View, name = 'Holidays_Packages_Packages'),
    path('Holidays-Packages',views.Holidays_Packages_List_View, name = 'Holidays_Packages'),
    path('Domestic-Packages',views.Domestic_Holiday_Package_List_View, name = 'Domestic_Packages'),
    path('Domestic_Package_Detail/<int:id>/', views.Domestic_Holiday_Package_Detail, name = 'Domestic_Package_Detail'),
    path('CentralAsia-Packages', views.Central_Asia_Packages_List_View, name = 'CentralAsia_Packages'),
    path('Europe-Packages', views.Europe_Packages_List_View, name = 'Europe_Packages'),
    path('MiddleEast-Packages', views.Middle_East_Packages_List_View, name = 'MiddleEast_Packages'),
    path('SouthEast-Asia-Packages', views.SouthEast_Asia_Packages_List_View, name = 'SouthEast_Asia_Packages'),
]

