from django.db import models
from django.contrib.auth.models import User
from status.models import  Challenge_Mind, Challenge_Body, Challenge_Skill

class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    challenge_body = models.ForeignKey(Challenge_Body, default=1, on_delete=models.SET_DEFAULT)
    body_challenge_status = models.BooleanField(default=False)
    challenge_mind = models.ForeignKey(Challenge_Mind, default=1, on_delete=models.SET_DEFAULT)
    mind_challenge_status = models.BooleanField(default=False)
    challenge_skill = models.ForeignKey(Challenge_Skill, default=1, on_delete=models.SET_DEFAULT)
    skill_challenge_status = models.BooleanField(default=True)
    acc_date = models.DateField(default=1)

    character  = models.CharField(default=1, max_length=100)
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
        return self.user.username

