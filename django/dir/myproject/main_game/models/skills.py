from django.db import models


class Skills(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=255)
    skill_description = models.TextField()