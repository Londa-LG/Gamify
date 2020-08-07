from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_items = models.IntegerField()
    inv_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.inv_name


