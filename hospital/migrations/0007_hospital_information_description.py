# Generated by Django 4.0.6 on 2022-08-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_patient_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital_information',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]