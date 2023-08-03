# appointments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/view/<str:doctor_id>/',views.doctor_info,name='doctor_info'),
    path('doctors/create/', views.create_doctor, name='create_doctor'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/view/<str:patient_id>/',views.patient_info,name='patient_info'),
    path('patients/create/', views.create_patient, name='create_patient'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<str:appointment_id>/',views.appointment,name='appointment'),
    path('appointments/book/', views.book_appointment, name='book_appointment'),
    path('appointments/edit/<str:appointment_id>',views.edit_appointment,name='edit_appointment'),
]
