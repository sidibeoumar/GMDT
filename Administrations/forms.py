from django import forms
from .models import Periode, Projet, Rapport, Stag

class PeridForm(forms.ModelForm):
    class Meta:
        model = Periode
        fields = ['date_debut', 'date_fin']


class Projetform(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'description']

        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control form-control-lg shadow-sm',
                'placeholder': 'Entrez le nom du projet',
                'style': 'font-weight: 600; font-size: 18px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control shadow-sm',
                'rows': 3,
                'placeholder': 'Décrivez brièvement le projet',
            }),
        }

    
    
    