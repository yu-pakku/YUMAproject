from django.db import models
from .afforestation_status import Afforestation_status


class Tree(models.Model):
    grows_area = models.ForeignKey(Afforestation_status, on_delete=models.CASCADE)
    tree_id = models.AutoField(primary_key=True)
    tree_age = models.IntegerField(default=0)