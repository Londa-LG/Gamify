import datetime
from .models import Status
from status.models import Challenge, Reward
from django.contrib.auth.models import User

def Date():
    td = datetime.date.today()
    return td

def CreateStatus():
    player = User.objects.get(username='Brian')
    first_challenge = Challenge.objects.get(name='Get ready to become strong')
    first_reward = Reward.objects.get(name='Legend in the making')
    date = datetime.date.today()
    Status.objects.create(user=player, challenge=first_challenge, rewards=first_reward, acc_date=date, character='Brian',age=1,level=1,job='None', title='Player', hp=100, strength=1, vitality=1, agility=1, intelligence=1)

