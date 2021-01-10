from django.db import models

# Create your models here.

class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    doctor_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    # specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    # register it in hospital app