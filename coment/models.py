from django.db import models

# Create your models here.
class Comment(models.Model):
    date = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    ananymous = models.BooleanField(default=False)
    interview_experience = models.CharField(max_length=10000)
    like_dislike_counter = models.IntegerField()
    hr_request = models.BooleanField(default=False)
    comp_name = models.CharField(max_length=64)