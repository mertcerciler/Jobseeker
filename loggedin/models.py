from django.db import models

class LoggedIn(models.Model):
    username  = models.CharField(max_length = 64)
    user_type = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
