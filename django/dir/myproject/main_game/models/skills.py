from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=255)
    skill_level = models.IntegerField(default=0)
    skill_script = models.IntegerField(default=0)
    skill_description = models.TextField()