# myapp/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    """
    Valide le mot de passe :
    - Minimum 12 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre
    - Doit contenir le symbole $
    """

    def validate(self, password, user=None):
        if len(password) < 12:
            raise ValidationError(_("Le mot de passe doit contenir au moins 12 caractères."))
        if not re.search(r'[A-Z]', password):
            raise ValidationError(_("Le mot de passe doit contenir au moins une majuscule."))
        if not re.search(r'[a-z]', password):
            raise ValidationError(_("Le mot de passe doit contenir au moins une minuscule."))
        if not re.search(r'\d', password):
            raise ValidationError(_("Le mot de passe doit contenir au moins un chiffre."))
        if '$' not in password:
            raise ValidationError(_("Le mot de passe doit contenir le symbole $."))
    
    def get_help_text(self):
        return _(
            "Votre mot de passe doit contenir au moins 12 caractères, "
            "inclure des majuscules, minuscules, chiffres et le symbole $."
        )