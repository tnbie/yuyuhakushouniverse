import datetime
import uuid 
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from item.models import Weapon, Armor, Leg, Boot, Bracer, Amulet, Ring, Shield

# Create your models here.
class Player(models.Model):
    # user information
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)

    # common features
    attack = models.PositiveSmallIntegerField(default=10)
    defense = models.PositiveSmallIntegerField(default=10)
    health = models.PositiveSmallIntegerField(default=10)
    mana = models.PositiveSmallIntegerField(default=10)
    spiritual_energy = models.PositiveSmallIntegerField(default=10)

    ## monitors
    actual_health = models.PositiveIntegerField(default=100)
    actual_mana = models.PositiveIntegerField(default=10)
    actual_spiritual_energy = models.PositiveIntegerField(default=10)

    ## updaters
    hp_update = models.DateTimeField(auto_now_add=True)
    mana_update = models.DateTimeField(auto_now_add=True)
    spiritual_energy_update = models.DateTimeField(auto_now_add=True) 

    # common stats
    strength = models.PositiveSmallIntegerField(default=10) 
    agility = models.PositiveSmallIntegerField(default=10) 
    intelligence = models.PositiveSmallIntegerField(default=10) 

    ## resources
    bank_account = models.FloatField(default=5000)
    player_account = models.FloatField(default=10000)

    # lifecycle
    level = models.PositiveSmallIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)


    # relations items
    # weapons = models.ManyToManyField(Weapon)
    # armors = models.ManyToManyField(Armor)
    # legs = models.ManyToManyField(Leg)
    # boots = models.ManyToManyField(Boot)
    # bracers = models.ManyToManyField(Bracer)
    # amulets = models.ManyToManyField(Amulet)
    # rings = models.ManyToManyField(Ring)
    # shields = models.ManyToManyField(Shield)
# 
    # # active items
    # weapons_active= models.ForeignKey(Weapon, null=True, related_name="+")
    # armors_active= models.ForeignKey(Armor, null=True, related_name="+")
    # legs_active = models.ForeignKey(Leg, null=True, related_name="+")
    # boots_active= models.ForeignKey(Boot, null=True, related_name="+")
    # bracers_active= models.ForeignKey(Bracer, null=True, related_name="+")
    # amulets_active= models.ForeignKey(Amulet, null=True, related_name="+")
    # rings_active= models.ForeignKey(Ring, null=True, related_name="+")
    # shields_active= models.ForeignKey(Shield, null=True, related_name="+")
    
    # pontos ao subir de nivel
    points = models.PositiveSmallIntegerField(default=0)

    # event date
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-nickname',)
        verbose_name_plural = 'Players'

             
    def __str__(self) -> str:
        return str(self.nickname)