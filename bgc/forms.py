from django import forms 
from .models import B_game

class B_gameForm(forms.ModelForm):
    class Meta:
        model = B_game
        fields = ['name','description']
        labels = {'name': '','description': ''}