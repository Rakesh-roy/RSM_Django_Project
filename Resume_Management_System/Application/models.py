from django.db import models


# Create your models here.
class RegistrationModel(models.Model):
    registration_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()
    doj = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100,default="pending")

