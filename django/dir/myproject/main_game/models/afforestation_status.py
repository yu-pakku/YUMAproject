from django.db import models
from django.contrib.auth.models import User
from .tree import Tree


class Afforestation_status(models.Model):
    Afforestation_id = models.AutoField(primary_key=True)
    Afforestation_name = models.CharField(max_length=255)
    Afforestation_size = models.IntegerField(default=1)
    author_id = models.OneToOneField(User, on_delete=models.CASCADE)
    trees = models.ForeignKey(Tree, on_delete=models.CASCADE)