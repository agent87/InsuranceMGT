# Generated by Django 4.1 on 2022-09-08 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0013_users_address_users_city_users_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultations',
            name='clinic_report',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='consultations',
            name='prescription',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='pharmacy',
            fields=[
                ('pharmacy_id', models.SmallAutoField(db_column='pharmacy_id', editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('pharmacist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pharmacies',
                'db_table': 'Pharmacy',
            },
        ),
    ]