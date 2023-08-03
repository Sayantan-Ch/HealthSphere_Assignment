
# appointments/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    id= models.TextField(max_length=10,unique=True,primary_key=True)
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    id= models.TextField(max_length=10,unique=True,primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    reason = models.TextField()
    id= models.TextField(max_length=10,unique=True,primary_key=True)
    def __str__(self):
        return f"{self.doctor} - {self.patient} - {self.date_time}"
