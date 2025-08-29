from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from Administrations.models import Stag

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Superuser')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
    

class User(AbstractUser):
    STATUS = [
        ('encour_de_taitement', 'Encour de traitement'),
        ('valid', 'Accepter'),
        ('rejet', 'Rejetez'),
        ('Encadrant', 'Encadre'),
    ]

    ROLE = [
        ('demandeur', 'Demandeur'),
        ('stagiaire', 'Stagiaire'),
        ('Encadreur', 'Encadreur'),
        ('Superuser', 'Superuser'),
    ]
    
    DOMAINE_ETUDE = [
        ('informatique', 'Informatique'),
        ('infographie', 'infographie'),
    ]

    email = models.EmailField(unique=True)
    cv = models.FileField(upload_to="cv_docs")
    telephone = models.CharField(max_length=10, verbose_name="Document", null=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLE, verbose_name="ROles", default="demandeur")
    status = models.CharField(max_length=25, choices=STATUS, verbose_name='Statut', default='traitement_encour')
    domaine_etude = models.CharField(max_length=35, choices=DOMAINE_ETUDE, verbose_name='domaine')
    encadreur = models.ForeignKey('self', related_name="stagiaire", on_delete=models.CASCADE, null=True, blank=True)
    stage = models.ForeignKey(Stag, related_name='stage', on_delete=models.CASCADE, null=True, blank=True)
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.last_name}--{self.first_name}"