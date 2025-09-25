from django import forms 
from .models import User
from Administrations.models import Stag
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import re

class UserForm(forms.ModelForm) :
        class Meta:
            model = User
            fields = ['username','first_name', 'last_name','email', 'cv', 'telephone', 'domaine_etude']


        widgets = {
            'username': forms.TextInput(attrs={
                'label': "Nom d'utilisateur ",
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
            'password1':forms.PasswordInput({
                'class': 'form-control',
                'placeholder': 'Mot de passe',
                'required': 'required'
            }),
            'password1':forms.PasswordInput({
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
            'Telephone': "Téléphone *",
            'role': "Rôle *",
            'status': "Statut *",
            'domaine_etude': "Domaine d'étude *",
            'password': "Mot de passe *",
           

        }
        password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe',
            'required': 'required'
        }),
        help_text="Votre mot de passe doit contenir au moins 12 caractères, majuscules, minuscules, chiffres et le symbole $."
    )

        password2 = forms.CharField(
            label="Confirmer le mot de passe",
            strip=False,
            widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirmer le mot de passe',
                'required': 'required'
            })
    )
        
        # ✅ Vérification du mot de passe (password1)
        def clean_password1(self):
            password = self.cleaned_data.get("password1")

            if not password:
                raise forms.ValidationError("❌ Le mot de passe est obligatoire.")

            # Vérif longueur
            if len(password) < 12:
                raise forms.ValidationError("❌ Le mot de passe doit contenir au moins 12 caractères.")

            # Vérif majuscules
            if not re.search(r"[A-Z]", password):
                raise forms.ValidationError("❌ Le mot de passe doit contenir au moins une majuscule.")

            # Vérif minuscules
            if not re.search(r"[a-z]", password):
                raise forms.ValidationError("❌ Le mot de passe doit contenir au moins une minuscule.")

            # Vérif chiffres
            if not re.search(r"[0-9]", password):
                raise forms.ValidationError("❌ Le mot de passe doit contenir au moins un chiffre.")

            # Vérif symbole $
            if "$" not in password:
                raise forms.ValidationError("❌ Le mot de passe doit contenir le symbole '$'.")

            return password


        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            password_confirm = cleaned_data.get("password_confirm")

            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Les mots de passe ne correspondent pas")

            return cleaned_data
        
User = get_user_model()

class CreateEncadreurForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe',
            'required': 'required'
        }),
        help_text="Votre mot de passe doit contenir au moins 12 caractères, avec majuscules, minuscules, chiffres et le symbole $."
    )

    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe',
            'required': 'required'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'telephone']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom d’utilisateur'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse email'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Téléphone'
            }),
        }

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        # Vérif longueur
        if len(password) < 12:
            raise forms.ValidationError("❌ Le mot de passe doit contenir au moins 12 caractères.")

        # Vérif majuscules
        if not re.search(r"[A-Z]", password):
            raise forms.ValidationError("❌ Le mot de passe doit contenir au moins une majuscule.")

        # Vérif minuscules
        if not re.search(r"[a-z]", password):
            raise forms.ValidationError("❌ Le mot de passe doit contenir au moins une minuscule.")

        # Vérif chiffres
        if not re.search(r"[0-9]", password):
            raise forms.ValidationError("❌ Le mot de passe doit contenir au moins un chiffre.")

        # Vérif symbole $
        if "$" not in password:
            raise forms.ValidationError("❌ Le mot de passe doit contenir le symbole '$'.")

        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("❌ Les mots de passe ne correspondent pas.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])  # hachage du mot de passe
        if commit:
            user.save()
        return user
    
class AffecteStageform(forms.ModelForm):
    stage = forms.ModelChoiceField(
        queryset=Stag.objects.all(),
        label="choisissez un stage",
        required=True
    )
    encadreur = forms.ModelChoiceField(
        queryset=User.objects.filter(role="Encadreur"),  # ⚡ uniquement les encadreurs
        label="Choisissez un encadreur",
        required=True
    )

    class Meta:
        model = User
        fields = ['stage', 'encadreur']

          



     


