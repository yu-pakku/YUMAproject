from django.db import models
from django.contrib.auth.models import User
from .status import Status

class Stats(models.Model):
    stats_od = models.AutoField(primary_key=True)
    status_id = models.OneToOneField(Status, on_delete=models.CASCADE)
    max_break_tree = models.IntegerField(default=0)
    break_trees = models.IntegerField(default=0)
