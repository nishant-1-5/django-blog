from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) # when a user is created then send this signal which is going to be recieved by this 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save();

## one more step, have to import the signals inside the users app.py ready function