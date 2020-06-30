from django.db import models
from coment.models import Comment
# Create your models here.
class Employee_Comment(Comment):
    work_experience = models.CharField(max_length=10000)
    position = models.CharField(max_length=64)
    salary_information = models.CharField(max_length=128)
    interview_process = models.CharField(max_length=10000)
    company_pros = models.CharField(max_length=10000)
    company_cons = models.CharField(max_length=10000)

