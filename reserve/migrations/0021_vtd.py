# Generated by Django 3.1 on 2020-08-20 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0020_auto_20200820_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='VTD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('permission', models.BooleanField(default=False)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserve.medicine')),
                ('visit_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserve.visittime')),
            ],
        ),
    ]