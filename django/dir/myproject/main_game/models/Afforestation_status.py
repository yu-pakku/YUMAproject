from django.db import models
from django.contrib.auth.models import User


class Afforestation_status(models.Model):
    author_id = models.OneToOneField(User, on_delete=models.CASCADE)
    afforestation_id = models.AutoField(primary_key=True)
    afforestation_name = models.CharField(max_length=255)
    afforestation_size = models.IntegerField(default=1)

