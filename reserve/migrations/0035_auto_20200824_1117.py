# Generated by Django 3.1 on 2020-08-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0034_visittime_full'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visittime',
            name='empty',
            field=models.CharField(default='True', max_length=20),
        ),
        migrations.AlterField(
            model_name='visittime',
            name='full',
            field=models.IntegerField(null=True),
        ),
    ]
