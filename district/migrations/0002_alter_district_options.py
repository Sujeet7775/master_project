# Generated by Django 5.2 on 2025-05-09 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['-created_at']},
        ),
    ]
