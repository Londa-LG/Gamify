from django.contrib import admin
from .models import Reward, Challenge_Body, Challenge_Mind, Challenge_Skill

admin.site.register(Challenge_Body)
admin.site.register(Challenge_Mind)
admin.site.register(Challenge_Skill)
admin.site.register(Reward)

