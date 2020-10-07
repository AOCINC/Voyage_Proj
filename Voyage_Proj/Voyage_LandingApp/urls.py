from django.urls import path
from Voyage_LandingApp import views

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('Enquiry-Form', views.Enquiry_View, name = 'Enquiry_Form'),
    path('Contact',views.Contact_View, name = 'Contact'),
    path('AboutUs',views.AboutUs_View, name = 'AboutUs'),
    path('Search-Wiki', views.search_places_wiki_veiw, name = 'Search_Wiki'),

]

