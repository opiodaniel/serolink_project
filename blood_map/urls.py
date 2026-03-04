from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.find_nearest_donors, name='find_donors'),
    path('donor_dashboard/', views.donor_dashboard, name='donor_dashboard'),

    path('hospital-dashboard/', views.hospital_dashboard, name='hospital_dashboard'),
]