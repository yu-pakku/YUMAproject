from django.db import models
from .power_up import PowerUp
from .status import Status


class UserPowerUp(models.Model):
    status_link = models.ForeignKey(Status,on_delete=models.CASCADE)
    power_up_link = models.ForeignKey(PowerUp,on_delete=models.CASCADE)
    power_up_level = models.IntegerField(default=0)
    acquired_at = models.DateTimeField(auto_now_add=True)
