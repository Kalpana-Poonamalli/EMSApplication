from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100, blank=True, null = True)
    dob = models.DateField()
    doj = models.DateField()
    department = models.CharField(max_length = 100)
    post = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipCode = models.IntegerField()
    state = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    leaveCount = models.IntegerField(default=0)
    on_leave = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Detail',kwargs={'pk':self.pk})
