from django import forms
from .models import DonorProfile, HospitalProfile

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ['blood_group', 'phone_number', 'is_available']
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+256...'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class HospitalProfileForm(forms.ModelForm):
    class Meta:
        model = HospitalProfile
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hospital Name'}),
        }