from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class States(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Districts(models.Model):
    states=models.ForeignKey(States,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    districts=models.ForeignKey(Districts,on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Person(models.Model):
    name=models.CharField(max_length=124, blank=True, null=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    states=models.ForeignKey(States,on_delete=models.CASCADE)
    districts=models.ForeignKey(Districts,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name