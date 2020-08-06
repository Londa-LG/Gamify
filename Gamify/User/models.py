from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
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

class Age(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.user.username}'