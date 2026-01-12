from django.db import models
from django.contrib.auth.models import User

class SkillExchange(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_offered = models.CharField(max_length=100)
    skill_requested = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_matched = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.skill_offered} -> {self.skill_requested}"
