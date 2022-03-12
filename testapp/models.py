from django.db import models 
from django.urls import reverse 


class Company(models.Model): 
    name=models.CharField(max_length=128) 
    location=models.CharField(max_length=64) 
    ceo=models.CharField(max_length=64)
    def __str__(self): 
        return self.name 
    def get_absolute_url(self): 
        return reverse('detail',kwargs={'pk':self.pk})


class Employee(models.Model): 
    eno=models.IntegerField() 
    name=models.CharField(max_length=128) 
    salary=models.FloatField() 
    company=models.ForeignKey(Company,related_name='employees',on_delete=models.CASCADE)