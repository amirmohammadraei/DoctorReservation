from phone_field import PhoneField
from django.db import models
from datetime import date


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    password = models.CharField(max_length=30)
    phone_number = PhoneField()
    verify = models.CharField(max_length=10)
    role = models.CharField(max_length=10, default='user')
    case_number = models.TextField(max_length=12)
    image = models.ImageField(default="profile.jpg", null=True, blank=True)
    doc1 = models.CharField(max_length=40, default='None')
    doc2 = models.CharField(max_length=40, default='None')
    sec1= models.CharField(max_length=40, default='None')
    sec2= models.CharField(max_length=40, default='None')


class VisitTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor', null=True)
    date = models.DateField(default=date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    empty = models.CharField(max_length=20, default="True")
    full = models.IntegerField(null=True)

    class Meta:
        ordering = ('date',)


class Medicine(models.Model):
    name = models.CharField(max_length=30)


class VTD(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    value = models.IntegerField()
    visit_time = models.ForeignKey(VisitTime, on_delete=models.CASCADE)
    permission = models.BooleanField(default=False)
