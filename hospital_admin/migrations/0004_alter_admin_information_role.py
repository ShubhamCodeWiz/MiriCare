# Generated by Django 4.0.6 on 2022-08-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_admin', '0003_alter_admin_information_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_information',
            name='role',
            field=models.CharField(blank=True, choices=[('hospital', 'hospital'), ('laboratory', 'laboratory'), ('pharmacy', 'pharmacy')], max_length=200, null=True),
        ),
    ]