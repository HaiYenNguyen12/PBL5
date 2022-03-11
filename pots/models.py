from pyexpat import model
from sre_parse import State
from django.db import models

# Create your models here.
class User (models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    
    
class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=50)
    time = models.FloatField(default=0)
    humidity = models.FloatField(default=0) 
    threadhold = models.IntegerField(default=0)
    
    
class Pest(models.Model):
    pest_name = models.CharField(max_length=50)
    
    
class Imgae(models.Model):
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
    imgURL = models.CharField(max_length=250)   
    
    
class State(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    state_pest = models.BooleanField()
    pest = models.ForeignKey(Pest, on_delete=models.CASCADE)
