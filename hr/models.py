from django.db import models
from user.models import User
# Create your models here.
class HR(User):
    company_name = models.CharField(max_length=128)
    
    
