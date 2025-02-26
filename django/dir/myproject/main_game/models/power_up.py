from django.db import models
from django.contrib.auth.models import User


class PowerUp(models.Model):
    power_up_id = models.AutoField(primary_key=True)
    power_up_name = models.CharField(max_length=255)
    power_up_level = models.IntegerField(default=1)
    power_up_type = models.CharField(max_length=255)
    power_up_description = models.TextField()
    author_id = models.ManyToManyField(User)
