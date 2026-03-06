from django import forms
from .models import Patient
import re

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'patient_id', 'mobile', 'gender', 'address', 'dob', 'doctor_name']
        widgets = {
            'dob': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match(r'^(98|97|96)\d{8}$', mobile):
            raise forms.ValidationError("Mobile must be 10 digits starting with 98, 97, or 96")
        return mobile