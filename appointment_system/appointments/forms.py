# appointments/forms.py

from django import forms
from .models import Appointment , Doctor , Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date_time', 'reason']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name' , 'specialization']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name' , 'email']