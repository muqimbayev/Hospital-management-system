# Generated by Django 5.0.1 on 2024-02-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_financial_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financial',
            name='check_number',
            field=models.BigIntegerField(unique=True),
        ),
    ]