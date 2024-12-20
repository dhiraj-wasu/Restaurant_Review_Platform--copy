from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    usertype= models.CharField(max_length=30)
    email=models.EmailField(max_length=50,null=True, blank=True)
    password=models.CharField(max_length=10,null=True, blank=True)

class customer(models.Model):
      user_name=models.CharField(max_length=255)
      user_email=models.EmailField()
      user_password=models.CharField(max_length=10,default="0",null=False)

class restaurant(models.Model):
      restaurant_name=models.CharField(max_length=255)
      restaurant_owner=models.CharField(max_length=255,null=True)
      owner_number=models.IntegerField(unique=True,null=True)
      owner_email=models.EmailField(max_length=254,unique=True,null=True)

class comments(models.Model):
      user_id=models.ForeignKey(customer,on_delete=models.CASCADE,null=True)
      restaurant_id=models.ForeignKey(restaurant,on_delete=models.CASCADE)
      Review=models.TextField()

class Leaderborad_backup(models.Model):
      restaurant_name=models.CharField(max_length=255)
      score=models.CharField(max_length=255)
      