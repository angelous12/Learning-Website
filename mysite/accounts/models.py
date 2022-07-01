from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
from page.models import Category
# Create your models here.


class UserCustom(AbstractUser):
    phone_number = models.CharField(max_length=20 , blank=True)
    phone_father = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    category = models.ManyToManyField(Category  , blank=True)
    token = models.CharField(max_length=200 , blank=True)  
    activeuser = models.BooleanField(default=False)                                                                                                                                                                                                                                                                                                                                                                                                                                 
     