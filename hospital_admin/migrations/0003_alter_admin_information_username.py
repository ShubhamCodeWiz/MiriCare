# Generated by Django 4.0.6 on 2022-08-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_admin', '0002_admin_information_featured_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_information',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]