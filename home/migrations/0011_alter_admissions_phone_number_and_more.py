# Generated by Django 5.0.1 on 2024-02-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_admissions_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissions',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='financial',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='history',
            name='user_phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
