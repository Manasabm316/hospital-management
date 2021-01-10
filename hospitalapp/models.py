from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Specialization(models.Model):
    specialization_list = models.CharField(max_length=50)

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    # specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)

class SlotRequest(models.Model):
    patientname = models.CharField(max_length=50)
    patientaddress = models.TextField(max_length=50)
    patientemail = models.EmailField(max_length=50)
    # patient_age = models.IntegerField()
    patientsymptoms = models.CharField(max_length=50)
    doctorname = models.CharField(max_length=50)

class Room(models.Model):
    # patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=20)

class SlotAllocation(models.Model):
    slotpatient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    # address = models.ForeignKey(User, on_delete=models.CASCADE) #reference should be address
    # age = models.ForeignKey(User, on_delete=models.CASCADE)
    # slotdoctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slotspecialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    slotroom_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    slotdate = models.DateField()
    slotgender = models.CharField(max_length=10)
    # slotroom_type = models.ForeignKey(Room, on_delete=models.CASCADE)

class Prescription(models.Model):
    patientname = models.CharField(max_length=20)
    patientsymptom = models.CharField(max_length=100)
    doc_prescription = models.TextField(max_length=200)
