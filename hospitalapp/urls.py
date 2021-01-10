from django.urls import path
from .import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('base', views.base, name='base'),
    path('nav',views.nav, name='nav'),
    path('footer', views.footer, name='footer'),
    path('loginoptions',views.loginoptions, name='loginoptions'),
    path('register', views.register, name='register'),
    path('patientlogin', views.patientlogin, name='patientlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('slotbooking', views.slot_request, name='slotbooking'),
    path('patient_prescription',views.patient_prescription, name='patient_prescription'),
    path('doctorlogin', views.doctorlogin, name='doctorlogin'),
    path('doc_dashboard', views.doc_dashboard, name='doc_dashboard'),
    path('doc_requests', views.doc_requests, name='doc_requests'),
    path('doc_prescription',views.doc_prescription, name='doc_prescription'),
    path('adminsite',views.adminsite, name='adminsite'),
    path('doc_registration',views.doc_registration , name='doc_registration'),
    path('logout', views.logoutUser, name='logout')
]