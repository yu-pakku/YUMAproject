from django.db import models
from django.contrib.auth.models import User


class Afforestation_status(models.Model):
    Afforestation_id = models.AutoField(primary_key=True)
    Afforestation_name = models.CharField(max_length=255)
    Afforestation_rank = models.IntegerField(default=1)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)