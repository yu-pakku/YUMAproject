from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    author_id = models.ManyToManyField(User)
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=255)
    skill_level = models.IntegerField(default=0)
    skill_type = models.CharField(max_length=255)
    skill_description = models.TextField()