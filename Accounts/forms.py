from django import forms 
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class UserForm(forms.ModelForm) :
    
    class Meta:
        model = User
        fields = ['username', 'password','first_name', 'last_name','email', 'cv', 'telephone', 'domaine_etude']


        widgets = {
            'username': forms.TextInput(attrs={
                'label': "Nom d'utilisateur *",
                'class': 'form-control',
                'placeholder': "Nom d'utilisateur",
                'required': 'required'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Prénom",
                'required': 'required'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Nom",
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Adresse e-mail",
                'required': 'required'
            }),
            'cv': forms.FileInput(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Téléphone",
                'required': 'required'
            }),
            'role': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
            'domaine_etude': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
            'password':forms.PasswordInput({
                'class': 'form-control',
                'placeholder': 'Mot de passe',
                'required': 'required'
            })
        }
         # 🔴 On ajoute "*" à chaque label obligatoire
        labels = {
            'username': "Nom d'utilisateur *",
            'first_name': "Prénom *",
            'last_name': "Nom *",
            'email': "Email *",
            'cv': "CV (PDF uniquement) *",
            'telephone': "Téléphone *",
            'role': "Rôle *",
            'status': "Statut *",
            'domaine_etude': "Domaine d'étude *",
            'password': "Mot de passe *",
        }

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            password_confirm = cleaned_data.get("password_confirm")

            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Les mots de passe ne correspondent pas")

            return cleaned_data
        



