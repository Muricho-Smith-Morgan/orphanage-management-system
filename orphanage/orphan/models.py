from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=50)
    children = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    situation = models.CharField(max_length=50)
    
   
    
   
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.name,self.id)

class Help(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    help_offered = models.CharField(max_length=30)
    
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.name,self.id)