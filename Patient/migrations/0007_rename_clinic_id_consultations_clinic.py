# Generated by Django 4.1 on 2022-09-05 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0006_consultations_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultations',
            old_name='clinic_id',
            new_name='clinic',
        ),
    ]