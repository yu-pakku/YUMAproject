from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    profile = models.TextField()
    icon = models.ImageField(upload_to='icons/')
    break_trees = models.IntegerField(default=0)
    author_id = models.OneToOneField(User, on_delete=models.CASCADE)



