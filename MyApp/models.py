from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   description = models.TextField(blank=True, null=True)
   count = models.PositiveIntegerField() 
   colors = models.ManyToManyField(Color, related_name='items', blank=True)
   
   def __str__(self):
        return f"{self.name}, {self.brand}"