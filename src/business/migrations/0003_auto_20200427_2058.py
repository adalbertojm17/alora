# Generated by Django 3.0.5 on 2020-04-28 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0002_store_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='manager',
        ),
        migrations.AddField(
            model_name='store',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
