# Generated by Django 3.0.5 on 2020-05-05 15:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20200505_1135'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='services',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='business.Service'),
            preserve_default=False,
        ),
    ]