# Generated by Django 5.1.5 on 2025-02-04 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_employeedetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetails',
            old_name='member',
            new_name='Employee',
        ),
    ]
