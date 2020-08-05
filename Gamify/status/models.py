from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(max_length=100)
    effects = models.TextField(max_length=100)

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    deadline = models.IntegerField()
    reward = models.CharField(max_length=100)

class Reward(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()