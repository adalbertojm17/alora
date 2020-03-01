# Generated by Django 3.0.3 on 2020-02-29 07:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10, null=True, region=None, unique=True),
        ),
    ]