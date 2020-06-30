from django.db import models
from user.models import User
# Create your models here.
class Jobseeker(User):
    resume = models.CharField(max_length=32)
    