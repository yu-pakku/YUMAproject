from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    profile = models.TextField()
    icon = models.ImageField(upload_to='icons/')
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)