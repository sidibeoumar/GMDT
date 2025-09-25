from django import forms
from .models import Periode, Projet, Rapport, Stag

from django import forms
from .models import Periode

class PeriodeForm(forms.ModelForm):
    class Meta:
        model = Periode
        fields = ['date_debut', 'date_fin']

        widgets = {
            'date_debut': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-lg shadow-sm',
                    'style': 'font-weight: 600; font-size: 18px;',
                    'type': 'date',  # ✅ permet d’avoir un calendrier HTML5
                }
            ),
            'date_fin': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-lg shadow-sm',
                    'style': 'font-weight: 600; font-size: 18px;',
                    'type': 'date',
                }
            ),
        }

    # ✅ Validation personnalisée
    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get("date_debut")
        date_fin = cleaned_data.get("date_fin")

        if date_debut and date_fin and date_fin < date_debut:
            self.add_error("date_fin", "La date de fin doit être postérieure à la date de début.")

        return cleaned_data


       



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
                'rows': 4,
                'placeholder': 'Décrivez brièvement le projet',
            })
        }


class StagForm(forms.ModelForm):
    class Meta:
        model = Stag
        fields = ['periode', 'projet']   # On ne prend pas rapport_stage
        widgets = {
            'periode': forms.Select(attrs={
                'class': 'form-control shadow-sm rounded-3'
            }),
            'projet': forms.Select(attrs={
                'class': 'form-control shadow-sm rounded-3'
            })
        }
    

    
    
    