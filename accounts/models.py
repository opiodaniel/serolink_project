from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Define roles
    IS_DONOR = 'donor'
    IS_HOSPITAL = 'hospital'

    ROLE_CHOICES = [
        (IS_DONOR, 'Donor'),
        (IS_HOSPITAL, 'Hospital'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=IS_DONOR
    )

    def __str__(self):
        return f"{self.username} ({self.role})"