# Generated by Django 2.2 on 2021-01-08 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0009_doctor_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slotrequest',
            old_name='doctor_name',
            new_name='doctorname',
        ),
        migrations.RenameField(
            model_name='slotrequest',
            old_name='patient_address',
            new_name='patientaddress',
        ),
        migrations.RenameField(
            model_name='slotrequest',
            old_name='patient_email',
            new_name='patientemail',
        ),
        migrations.RenameField(
            model_name='slotrequest',
            old_name='patient_name',
            new_name='patientname',
        ),
        migrations.RenameField(
            model_name='slotrequest',
            old_name='patient_symptom',
            new_name='patientsymptom',
        ),
    ]
