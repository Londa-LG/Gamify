from django.contrib.auth.models import User
from .models import Status
from status.models import Challenge_Body, Challenge_Mind, Challenge_Skill
import datetime


def AssignPoints(request):
    mind = request.user.status.challenge_mind.reward
    mind = mind.split(",")
    body = request.user.status.challenge_body.reward
    body = body.split(",")
    skill = request.user.status.challenge_skill.reward
    skill = skill.split(",")
    for atr in mind:
        if atr == "intelligence":
            current = request.user.status
            current.intelligence += 1
            current.save()
        if atr == "strength":
            current = request.user.status
            current.strength += 1
            current.save()
        if atr == "agility":
            current = request.user.status
            current.agility += 1
            current.save()
        if atr == "vitality":
            current = request.user.status
            current.vitality += 1
            current.save()

    for atr in body:
        if atr == "intelligence":
            current = request.user.status
            current.intelligence += 1
            current.save()
        if atr == "strength":
            current = request.user.status
            current.strength += 1
            current.save()
        if atr == "agility":
            current = request.user.status
            current.agility += 1
            current.save()
        if atr == "vitality":
            current = request.user.status
            current.vitality += 1
            current.save()

    for atr in skill:
        if atr == "intelligence":
            current = request.user.status
            current.intelligence += 1
            current.save()
        if atr == "strength":
            current = request.user.status
            current.strength += 1
            current.save()
        if atr == "agility":
            current = request.user.status
            current.agility += 1
            current.save()
        if atr == "vitality":
            current = request.user.status
            current.vitality += 1
            current.save()



def CreateStatus(username):
    user = User.objects.get(username=username)
    date = datetime.date.today()
    mind = Challenge_Mind.objects.get(name='Building your Foundation(mind)')
    body = Challenge_Body.objects.get(name='Building your Foundation(body)')
    skill = Challenge_Skill.objects.get(name='Building your Foundation(skill)')
    Status.objects.create(user=user, challenge_body=body, challenge_mind=mind, challenge_skill=skill, acc_date=date, character='Noob',age=11 , level=0, job="None", title="Player", hp=100, strength=0, vitality=0, agility=0, intelligence=0)
