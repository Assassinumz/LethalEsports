from unittest.util import _MAX_LENGTH
from django.db import models
from traitlets import default
#from djongo import models

# Create your models here.

class Carousel(models.Model):
    
    link = models.CharField(default="#", max_length=600)
    image = models.URLField(default="https://as2.ftcdn.net/v2/jpg/03/95/37/19/1000_F_395371923_x2IUqSOYDCQeBCx3auKcK3EbyzNjhlNV.jpg")

class Event(models.Model):
    
    title = models.CharField(default="#", max_length=600)
    location = models.CharField(default="Online", max_length=100)
    image = models.CharField(default="#", max_length=600)
    link = models.CharField(default="#", blank=True, max_length=600)
    description = models.TextField(default="#")
    date = models.DateField()


class Management(models.Model):
    
    first_name = models.CharField(default="null", max_length=100)
    last_name = models.CharField(default="null", max_length=100)
    ign = models.CharField(default="null", max_length=60)
    doj = models.DateField()
    image = models.CharField(default="#", max_length=600)
    description = models.TextField(default="#")
    #streams = models.TextField(default="#")

    instagram_followers = models.CharField(null=True, max_length=60, blank=True)
    instagram_link = models.CharField(max_length=600, null=True)

    youtube_subs = models.CharField(null=True, max_length=60, blank=True)
    youtube_link = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.ign

class Player(models.Model):
    
    games = (
        ('valorant', 'Valorant'),
        ('csgo', 'CSGO'),
    )
    first_name = models.CharField(default="null", max_length=100)
    last_name = models.CharField(default="null", max_length=100)
    ign = models.CharField(default="null", max_length=60)
    doj = models.DateField()
    image = models.CharField(default="#", max_length=600)
    description = models.TextField(default="#")
    game = models.TextField(choices=games, default="valorant", blank=True)
    streams = models.TextField(null=True, blank=True)

    instagram_followers = models.CharField(null=True, max_length=60, blank=True)
    instagram_link = models.CharField(max_length=600, null=True, blank=True)

    youtube_subs = models.CharField(null=True, max_length=60, blank=True)
    youtube_link = models.CharField(max_length=600, null=True, blank=True)

    twitter_subs = models.CharField(null=True, max_length=60, blank=True)
    twitter_link = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.ign

class Creator(models.Model):
    
    platforms = (
        ('youtube', 'youtube'),
        ('twitch', 'twitch'),
    )
    first_name = models.CharField(default="null", max_length=100)
    last_name = models.CharField(default="null", max_length=100)
    ign = models.CharField(default="null", max_length=60)
    doj = models.DateField()
    image = models.CharField(default="#", max_length=600)
    description = models.TextField(default="#")
    platform = models.TextField(choices=platforms, default="youtube", blank=True)
    streams = models.TextField(null=True, blank=True)

    instagram_followers = models.CharField(null=True, max_length=60, blank=True)
    instagram_link = models.CharField(max_length=600, null=True, blank=True)

    youtube_subs = models.CharField(null=True, max_length=60, blank=True)
    youtube_link = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
        return self.ign