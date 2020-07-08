# Core Django imports.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Blog application imports.
from .models.author_models import Profile


# Creates author profile immediately an account is created for her/him.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Saves author profile automatically after creating the profile.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
