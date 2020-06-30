from django.db import models
from user.models import User
# Create your models here.
class Employee(User):
    position = models.CharField(max_length=32)
    salary = models.IntegerField()
    resume = models.CharField(max_length=32)
  
    