from django.db import models
from inventory.models import Inventory

class Item(models.Model):
    storage = models.ForeignKey(Inventory,default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    effects = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    deadline = models.IntegerField()
    reward = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reward(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name