from django import forms 
from .models import B_game,Review

class B_gameForm(forms.ModelForm):
    class Meta:
        model = B_game
        fields = ['name','description']
        labels = {'name': '','description': ''}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text','stars']
        labels = {'text': '','stars': ''}
        widgets = {'text' : forms.Textarea(attrs={'cols': 80})}