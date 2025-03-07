from django.db import models
from .skills import Skills
from .status import Status


class UserSkills(models.Model):
    status_link = models.ForeignKey(Status,on_delete=models.CASCADE)
    skills_link = models.ForeignKey(Skills,on_delete=models.CASCADE)
    skills_level = models.IntegerField(default=0)
    acquired_at = models.DateTimeField(auto_now_add=True)
