from django.db import models


class Inventory(models.Model):
    size = models.IntegerField()
    item_number = models.IntegerField()


