# Generated by Django 5.0.1 on 2024-02-06 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_admissions_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admissions',
            old_name='time',
            new_name='Time',
        ),
    ]
