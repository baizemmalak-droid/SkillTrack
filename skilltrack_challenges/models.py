from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# =======================
# SKILL
# =======================
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=10, default="🧠")

    def __str__(self):
        return self.name


# =======================
# CHALLENGE
# =======================
class Challenge(models.Model):
    LEVEL_CHOICES = [
        ("easy", "Easy"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="challenges")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    points = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.skill.name} ({self.level})"


# =======================
# CHALLENGE SUBMISSION
# =======================
class ChallengeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    solution = models.TextField()
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "challenge")

    def __str__(self):
        return f"{self.user.username} - {self.challenge.title}"


# =======================
# USER PROFILE
# =======================
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


# =======================
# BADGE
# =======================
class Badge(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


# =======================
# USER BADGE
# =======================
class UserBadge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "badge")

    def __str__(self):
        return f"{self.user.username} - {self.badge.name}"


# =======================
# MOTIVATION MESSAGE
# =======================
class MotivationMessage(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


# =======================
# SIGNAL: CREATE PROFILE
# =======================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
