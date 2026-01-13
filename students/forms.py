from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['specialty', 'languages', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }