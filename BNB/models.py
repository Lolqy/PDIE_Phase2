from django.db import models

# Create your models here.

class Worker(models.Model):
    WorkersId = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=20)
    sec_name = models.CharField(max_length=25)
    
    
class Customer(models.Model):
    CustId = models.CharField(max_length=5,primary_key=True)
    name = models.CharField(max_length=25)
    pax = models.CharField(max_length=10)
    date = models.DateField(max_length=20)
    time = models.TimeField(auto_now=False, auto_now_add=False,)
    activity = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=[
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('waiting', 'Waiting')
    ], default='waiting')