# Generated by Django 4.1 on 2022-09-04 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultations',
            name='clinic_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Patient.clinics'),
        ),
    ]
