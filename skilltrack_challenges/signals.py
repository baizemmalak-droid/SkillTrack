from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ChallengeSubmission, UserBadge, Badge


@receiver(post_save, sender=ChallengeSubmission)
def give_badge_on_approval(sender, instance, created, **kwargs):
    if instance.is_approved:
        user = instance.user

        badge = Badge.objects.filter(name="First Step").first()
        if badge:
            UserBadge.objects.get_or_create(user=user, badge=badge)



