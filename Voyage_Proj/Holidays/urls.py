from django.urls import path
from Holidays import views

urlpatterns = [
    path('Holidays-Packages-Upload',views.Holidays_PackagesUpload_View, name = 'Holidays_Packages_Packages'),
    path('Holidays-Packages',views.Holidays_Packages_List_View, name = 'Holidays_Packages'),
    path('All_Holidays_Package_Detail/<int:id>/', views.All_Holidays_Package_Detail, name = 'All_Holidays_Package_Detail'),
    path('Domestic-Packages',views.Domestic_Holiday_Package_List_View, name = 'Domestic_Packages'),
    path('Domestic_Package_Detail/<int:id>/', views.Domestic_Holiday_Package_Detail, name = 'Domestic_Package_Detail'),
    path('CentralAsia-Packages', views.Central_Asia_Packages_List_View, name = 'CentralAsia_Packages'),
    path('Central_Aisa_Package_Detail/<int:id>/', views.Central_Asia_Package_Detail, name = 'Central_Aisa_Package_Detail'),
    path('Europe-Packages', views.Europe_Packages_List_View, name = 'Europe_Packages'),
    path('Europe_Package_Detail/<int:id>/', views.Europe_Package_Detail, name = 'Europe_Package_Detail'),
    path('MiddleEast-Packages', views.Middle_East_Packages_List_View, name = 'MiddleEast_Packages'),
    path('MiddleEast_Package_Detail/<int:id>/', views.MiddleEast_Package_Detail, name = 'MiddleEast_Package_Detail'),
    path('SouthEast-Asia-Packages', views.SouthEast_Asia_Packages_List_View, name = 'SouthEast_Asia_Packages'),
    path('SouthEast_Asia_Package_Detail/<int:id>/', views.SouthEast_Asia_Packages_Detail, name = 'SouthEast_Asia_Package_Detail'),
]

