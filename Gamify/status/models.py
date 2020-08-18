from django.db import models


class Challenge_Body(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    deadline = models.IntegerField()
    reward = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Challenge_Mind(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    deadline = models.IntegerField()
    reward = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Challenge_Skill(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    deadline = models.IntegerField()
    reward = models.CharField(max_length=100)

    def __str__(self):
        return self.name

