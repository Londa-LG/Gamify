import datetime
from .models import Status
from inventory.models import Inventory
from status.models import Challenge, Reward, Item
from django.contrib.auth.models import User

def Date():
    td = datetime.date.today()
    return td

def CreatePlayer(name):
    player = User.objects.get(username=name)
    first_challenge = Challenge.objects.get(name='Get ready to become strong')
    first_reward = Reward.objects.get(name='Legend in the making')
    date = datetime.date.today()
    Status.objects.create(user=player, challenge=first_challenge, rewards=first_reward, acc_date=date, character=name,age=1,level=1,job='None', title='Player', hp=100, strength=1, vitality=1, agility=1, intelligence=1)

def CreateInventory(name):
    player = User.objects.get(username=name)
    Inventory.objects.create(user=player, no_items=0, inv_name=f"{name}'s Inventory")

def BasicItem(name):
    player = User.objects.get(username=name)
    inv = Inventory.objects.get(user=player)
    inv.no_items = inv.no_items + 1
    Item.objects.create(storage=inv, name="Basic long Sword", level=1, effects="None")
