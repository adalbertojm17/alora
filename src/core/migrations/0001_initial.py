# Generated by Django 3.0.4 on 2020-04-03 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('business', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('service',
                 models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Service')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
            ],
            options={
                'verbose_name_plural': 'Order Items',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_at', models.DateTimeField()),
                ('dropoff_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('current_status', models.CharField(
                    choices=[('P', 'Processed'), ('PU', 'Picked up'), ('CL', 'Cleaning'), ('CP', 'Complete'),
                             ('ER', 'Enroute'), ('D', 'Delivered')], max_length=2)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                              to=settings.AUTH_USER_MODEL)),
                ('dropoff_location',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to='addresses.Address')),
                ('items', models.ManyToManyField(to='core.Item')),
                ('pickup_location',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='addresses.Address')),
                ('store',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Store')),
            ],
        ),
    ]
