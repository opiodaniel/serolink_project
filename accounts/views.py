from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from blood_map.models import DonorProfile, HospitalProfile
from django.contrib.gis.geos import Point
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import uuid


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.role == 'donor':
                DonorProfile.objects.create(
                    user=user,
                    location=Point(0, 0),
                    phone_number="+256700000000", # Temporary placeholder
                    blood_group="O+"              # Default placeholder
                )
            elif user.role == 'hospital':
                HospitalProfile.objects.create(
                    user=user,
                    name=user.username,
                    location=Point(0, 0),
                    license_number = f"TEMP-{uuid.uuid4().hex[:8]}"  # Creates a unique temp ID
                )
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def profile_redirect_view(request):
    if request.user.role == 'donor':
        return redirect('update_location') # Send donors to their map
    else:
        return redirect('find_donors') # Send hospitals to the search
