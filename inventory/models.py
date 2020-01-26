from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    content = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    amount = models.PositiveIntegerField()
    # account

    def __str__(self):
        return self.title
