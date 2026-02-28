from django.contrib.gis.db import models  # IMPORT FROM GIS.DB, NOT DB
from django.conf import settings


class DonorProfile(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    # Links to our Custom User model in accounts
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='donor_profile'
    )
    phone_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)

    # PointField stores Longitude and Latitude as a geometric point
    # SRID 4326 is the global standard for GPS (WGS84)
    location = models.PointField(srid=4326)

    last_donated = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} ({self.blood_group})"


class HospitalProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hospital_profile'
    )
    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, unique=True)

    # The Hospital's coordinates serve as the center point for searches
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name
