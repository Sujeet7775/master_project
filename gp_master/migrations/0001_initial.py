# Generated by Django 5.2 on 2025-05-09 12:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('block', '0001_initial'),
        ('district', '0002_alter_district_options'),
        ('package', '0002_alter_package_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPMaster',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gp_name', models.CharField(max_length=255)),
                ('lgd_code', models.CharField(max_length=100)),
                ('phase', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('gp_status', models.CharField(max_length=100)),
                ('covered', models.BooleanField(default=False)),
                ('sr_status', models.CharField(max_length=100)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gps', to='block.block')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gps', to='district.district')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gps', to='package.package')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
