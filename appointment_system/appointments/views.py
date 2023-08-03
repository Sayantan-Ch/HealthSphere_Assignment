# appointments/views.py

from django.shortcuts import render, redirect , get_object_or_404
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm , DoctorForm , PatientForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctor_list.html', {'doctors': doctors})

def doctor_info(request,doctor_id):
    doctor = Doctor.objects.filter(id=doctor_id)
    appointments = Appointment.objects.filter(doctor=doctor[0])
    return render(request,'appointments/doctor_info.html', {'appointments': appointments , 'doctors': doctor})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'appointments/create_patient.html', {'form': form})

def patient_info(request,patient_id):
    patient = Patient.objects.filter(id=patient_id)
    appointments = Appointment.objects.filter(patient=patient[0])
    return render(request,'appointments/patient_info.html', {'appointments': appointments , 'patients':patient})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'appointments/patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/edit_appointment.html', {'form': form, 'appointment': appointment})

def appointment(request,appointment_id):
    appointments = Appointment.objects.filter(id=appointment_id)
    return render(request,'appointments/appointment_list.html', {'appointments': appointments})


def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'appointments/create_doctor.html', {'form': form})

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'appointments/create_patient.html', {'form': form})
def book_appointment(request):
    if request.method == 'POST':
        print(request)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})
