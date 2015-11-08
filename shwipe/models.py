# https://docs.djangoproject.com/en/1.8/topics/db/models/
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.URLField(blank=True, null=True, unique=True)
    price = models.CharField(max_length=255)
    shwiped = models.BooleanField(default=False)
    
    def __str__(self):
        return unicode(self.name)

class Shwipe(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    direction = models.CharField(max_length=100, choices=(('Left', 'Left'),('Right', 'Right')))
