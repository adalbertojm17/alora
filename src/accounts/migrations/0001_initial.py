# Generated by Django 3.0.3 on 2020-03-18 16:04

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=35, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('phone',
                 phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=15, null=True, region=None,
                                                                unique=True)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_business', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
