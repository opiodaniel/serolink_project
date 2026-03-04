from django.shortcuts import render, redirect
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from .models import DonorProfile, HospitalProfile

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.gis.geos import Point
from django.shortcuts import render
from django.http import JsonResponse
from .models import DonorProfile
from .forms import DonorProfileForm

def home_view(request):
    # Count available donors to show on the home page
    donor_count = DonorProfile.objects.filter(is_available=True).count()

    context = {
        'donor_count': donor_count,
    }
    return render(request, 'home.html', context)

def find_nearest_donors(request):
    # 1. Ensure the user is a Hospital
    if request.user.role != 'hospital':
        return render(request, 'blood_map/error.html', {
            'message': "Only Hospital accounts can access the donor search engine."
        })

    # 2. Get the specific hospital profile for this user
    try:
        hospital = request.user.hospital_profile
    except HospitalProfile.DoesNotExist:
        return render(request, 'blood_map/error.html', {
            'message': "You are logged in as a hospital, but no profile was found. Please set up your facility in 'My Facility tab'."
        })

    # 1. Get filters from the URL
    blood_group_filter = request.GET.get('group')
    # Default to 10 if not provided, and convert to integer
    try:
        radius_km = int(request.GET.get('radius', 10))
    except ValueError:
        radius_km = 10

    # 2. Start the query with the dynamic radius
    donors_qs = DonorProfile.objects.filter(
        location__distance_lte=(hospital.location, D(km=radius_km)),
        is_available=True
    )

    if blood_group_filter:
        # Clean up the '+' if it came in as a space
        blood_group_filter = blood_group_filter.replace(' ', '+')
        donors_qs = donors_qs.filter(blood_group=blood_group_filter)

    nearby_donors = donors_qs.annotate(
        distance=Distance('location', hospital.location)
    ).order_by('distance')

    context = {
        'hospital': hospital,
        'donors': nearby_donors,
        'selected_group': blood_group_filter,
        'radius': radius_km,
        'blood_groups': ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']  # Add this line
    }

    return render(request, 'blood_map/search_results.html', context)



@login_required
def donor_dashboard(request):
    # 1. Check if the user is a donor
    if request.user.role != 'donor':
        return render(request, 'blood_map/error.html', {
            'message': "Access Denied. Only Donor accounts can manage a donor profile."
        })

    try:
        profile = request.user.donor_profile
    except DonorProfile.DoesNotExist:
        return render(request, 'blood_map/error.html', {
            'message': "Profile not found. Please contact support."
        })

    if request.method == "POST":
        # Check if it's a Map update (AJAX) or a Form update (Standard POST)
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        if lat and lng:  # Handle Map Update
            profile.location = Point(float(lng), float(lat))
            profile.save()
            return JsonResponse({'status': 'success'})

        # Handle Blood Group/Phone Update
        form = DonorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('donor_dashboard')

    else:
        form = DonorProfileForm(instance=profile)

    return render(request, 'blood_map/donor_dashboard.html', {
        'profile': profile,
        'form': form
    })


from .forms import HospitalProfileForm, DonorProfileForm  # Import both


@login_required
def hospital_dashboard(request):
    # Ensure only hospitals can access this
    if request.user.role != 'hospital':
        return redirect('home')

    try:
        profile = request.user.hospital_profile
    except HospitalProfile.DoesNotExist:
        return render(request, 'blood_map/error.html', {'message': 'Hospital profile not found.'})

    if request.method == "POST":
        # Check for AJAX Map update
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        if lat and lng:
            profile.location = Point(float(lng), float(lat))
            profile.save()
            return JsonResponse({'status': 'success'})

        # Handle Name change
        form = HospitalProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('hospital_dashboard')
    else:
        form = HospitalProfileForm(instance=profile)

    return render(request, 'blood_map/hospital_dashboard.html', {
        'profile': profile,
        'form': form
    })