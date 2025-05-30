# Generated by Django 5.2 on 2025-05-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('Supervisor', 'Supervisor'), ('Director', 'Director')], max_length=20)),
            ],
            options={
                'verbose_name': 'User Profile',
                'ordering': ['-created_at'],
                'unique_together': {('user_type',)},
            },
        ),
    ]
