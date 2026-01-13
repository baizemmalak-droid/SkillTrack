from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} (Level {self.level})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    xp = models.IntegerField(default=0)
    badges = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()