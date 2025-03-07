from django.db import models
from .afforestation_status import Afforestation_status

class Tree(models.Model):
    tree_id = models.AutoField(primary_key=True)
    tree_age = models.IntegerField(default=0)
    tree_rank = models.IntegerField(default=1)
    tree_completed = models.IntegerField(default=0)
    afforestation = models.ForeignKey(Afforestation_status ,on_delete=models.CASCADE)