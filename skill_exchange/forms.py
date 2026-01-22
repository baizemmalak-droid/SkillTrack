from django import forms
from .models import UserSkill

class SkillForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        fields = ['skill', 'level']