# Generated by Django 3.1 on 2020-08-22 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0023_auto_20200822_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='visittime',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='visittime',
            name='empty',
            field=models.BooleanField(default=False),
        ),
    ]