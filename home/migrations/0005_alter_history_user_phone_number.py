# Generated by Django 5.0.1 on 2024-02-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_history_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='user_phone_number',
            field=models.CharField(max_length=30),
        ),
    ]