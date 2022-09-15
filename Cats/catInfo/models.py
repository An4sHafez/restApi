from django.db import models


class Cat(models.Model):
  name = models.CharField(max_length=20)
  breeds= models.CharField(max_length=20)
  color= models.CharField(max_length=20,null=True)
  #img = models.ImageField()
  