
from django.db import models
from coment.models import Comment
# Create your models here.
class Requested_Coment(Comment):
    work_experience = models.CharField(max_length=10000)
    interview_process = models.CharField(max_length=10000)
    company_pros = models.CharField(max_length=10000)
    company_cons = models.CharField(max_length=10000)
    cmp_name = models.CharField(max_length=64)