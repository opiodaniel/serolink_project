from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.find_nearest_donors, name='find_donors'),
    path('update-location/', views.update_location_view, name='update_location'),

    path('hospital-dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
]