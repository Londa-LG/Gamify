from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Status(models.Model):
    age = models.IntegerField()
    level = models.IntegerField()
    job = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    hp = models.IntegerField()
    strength = models.IntegerField()
    vitality = models.IntegerField()
    agility = models.IntegerField()
    intelligence = models.IntegerField()

    class Meta:
        verbose_name_plural = "Status"
