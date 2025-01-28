from django import forms
from .models import AboutMe, Project

class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['title', 'description']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']
