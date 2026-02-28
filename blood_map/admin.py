from django.contrib.gis import admin
from .models import DonorProfile, HospitalProfile


# We use GISModelAdmin to activate the Map Widget
@admin.register(DonorProfile)
class DonorAdmin(admin.GISModelAdmin):
    list_display = ('user', 'blood_group', 'is_available', 'location')
    list_filter = ('blood_group', 'is_available')

    # Coordinates for Uganda (Centering the map)
    default_lat = 1.3733
    default_lon = 32.2903
    default_zoom = 7

    # Uses OpenStreetMap instead of the default vector map
    gis_widget_kwargs = {
        'attrs': {
            'default_lat': 1.3733,
            'default_lon': 32.2903,
        }
    }


@admin.register(HospitalProfile)
class HospitalAdmin(admin.GISModelAdmin):
    list_display = ('name', 'location')

    # Coordinates for Uganda (Centering the map)
    default_lat = 1.3733
    default_lon = 32.2903
    default_zoom = 7

    # Uses OpenStreetMap instead of the default vector map
    gis_widget_kwargs = {
        'attrs': {
            'default_lat': 1.3733,
            'default_lon': 32.2903,
        }
    }
