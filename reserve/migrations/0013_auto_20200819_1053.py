# Generated by Django 3.1 on 2020-08-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0012_appointment_secretary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
