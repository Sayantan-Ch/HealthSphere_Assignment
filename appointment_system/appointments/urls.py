# appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<str:doctor_id>/',views.doctor_appointment,name='doctor_appointment'),
    path('patient/<str:patient_id>/',views.patient_appointment,name='patient_appointment'),
    path('appointments/edit/<str:appointment_id>',views.edit_appointment,name='edit_appointment'),
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/book/', views.book_appointment, name='book_appointment'),
    path('doctors/create/', views.create_doctor, name='create_doctor'),
    path('patients/create/', views.create_patient, name='create_patient'),
]
