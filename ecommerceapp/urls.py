from django.urls import path
from ecommerceapp.views import RegisterUser,ProtectedView,TourpackageView,TourpackagelistView



urlpatterns = [
    path('RegisterUser/',RegisterUser.as_view(),name='RegisterUser'),
    path('ProtectedView/',ProtectedView.as_view(),name='ProtectedView'),
    path('TourpackageView/',TourpackageView.as_view(),name='TourpackageView'),
    path('TourpackagelistView/',TourpackagelistView.as_view(),name='TourpackagelistView'),
   
     
]