from django.db import models
from user.models import User

class Admin(User):
    admin_name = models.CharField(max_length=128)
