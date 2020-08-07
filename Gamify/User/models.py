from django.db import models
from django.contrib.auth.models import User
from status.models import Reward, Challenge

class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE)
    rewards = models.OneToOneField(Reward, on_delete=models.CASCADE)
    acc_date = models.DateField(default=1)

    age = models.IntegerField(default=1)
    level = models.IntegerField(default=1)
    job = models.CharField(max_length=100,default="None")
    title = models.CharField(max_length=100,default="None")
    hp = models.IntegerField(default=100)
    strength = models.IntegerField(default=1)
    vitality = models.IntegerField(default=1)
    agility = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.title

