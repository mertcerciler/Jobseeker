from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 32)
    user_type = models.CharField(max_length = 32)
    user_type = models.CharField(max_length = 32)
    password = models.CharField(max_length = 32)
    name = models.CharField(max_length = 32)
    apartment_no = models.IntegerField()
    street = models.CharField(max_length = 32)
    city = models.CharField(max_length = 32)
    zip_code = models.CharField(max_length = 64)
    age = models.IntegerField()
    e_mail = models.CharField(max_length = 128)
    def __str__(self):
      return self.username