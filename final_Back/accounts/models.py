from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    age=models.IntegerField()
    sex=models.CharField(max_length=5)
    
