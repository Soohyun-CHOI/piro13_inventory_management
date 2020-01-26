from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    amount = models.PositiveIntegerField(null=True)
    # account

    def __str__(self):
        return self.title
