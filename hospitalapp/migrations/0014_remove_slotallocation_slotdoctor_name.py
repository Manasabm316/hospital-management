# Generated by Django 3.1.4 on 2021-01-09 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0013_auto_20210108_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotallocation',
            name='slotdoctor_name',
        ),
    ]
