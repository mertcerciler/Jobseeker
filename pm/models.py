from django.db import models
from user.models import User
class pm(models.Model):
    date = models.CharField(max_length = 32)
    content = models.CharField(max_length = 1024)
    seen_time = models.CharField(max_length = 32)
    user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.content

