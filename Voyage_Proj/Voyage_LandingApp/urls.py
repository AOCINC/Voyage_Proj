from django.urls import path
from Voyage_LandingApp import views

urlpatterns = [
    path('',views.home_view, name = 'home')

]

