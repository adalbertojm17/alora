# Generated by Django 3.0.5 on 2021-03-09 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200505_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servingareas',
            old_name='zipcode',
            new_name='zip_code',
        ),
        migrations.RenameField(
            model_name='store',
            old_name='servingareas',
            new_name='serving_areas',
        ),
    ]