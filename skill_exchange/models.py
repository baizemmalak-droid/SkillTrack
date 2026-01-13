from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SkillRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # الوقت الذي تم فيه الطلب

    def __str__(self):
        return f"{self.user.username} requests {self.skill.name}"