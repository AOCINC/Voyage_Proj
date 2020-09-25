from django.urls import path
from Voyage_LandingApp import views

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('Enquiry-Form', views.Enquiry_View, name = 'Enquiry_Form'),

]

