# Generated by Django 2.2 on 2021-01-08 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0011_auto_20210108_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slotrequest',
            old_name='patientsymptom',
            new_name='patientsymptoms',
        ),
    ]
