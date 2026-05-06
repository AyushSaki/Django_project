from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    fname=models.CharField(max_length=100)
    contact=models.CharField(max_length=150)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=150)
    message=models.TextField()
    
    def __str__(self):
        return self.fname
    
    
class Register(models.Model):
    name=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    contact=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    password=models.CharField(max_length=150)
    message=models.TextField()
    hobbies = models.JSONField(default=list)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='male')
    
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    fileupload = models.FileField(upload_to='uploads/', max_length=1000, null=True, default=None)



    def __str__(self):
        return self.name
