from django.db import models

# Create your models here.
class Companies(models.Model):
    company_name = models.CharField(max_length = 128)
    location = models.CharField(max_length=32)
    e_mail = models.CharField(max_length=64)
    rating = models.IntegerField()
    def __str__(self):
        return self.company_name
    