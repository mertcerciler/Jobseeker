from django.db import models

# Create your models here.
class Offerings(models.Model):
    company_name = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 32)
    position = models.CharField(max_length = 32)
    salary = models.IntegerField()
    description = models.CharField(max_length = 1000)
    advertising_date = models.CharField(max_length=32)
    closing_date = models.CharField(max_length=32)
    def __str__(self):
        return self.company_name