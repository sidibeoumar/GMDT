from django.db import models

# Create your models here.
class Rapport(models.Model):
    rapport  = models.FileField(upload_to="rapport_doc")
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.rapport
    
class Projet(models.Model):
    nom = models.CharField(max_length=25)
    description = models.CharField(max_length=255, verbose_name="Description")
    
    def __str__(self):
        return self.nom
    
    def get_file_name(self)->str :
        return self.rapport.name.split('/')[-1]
    
class Periode(models.Model):
    date_debut = models.DateField(verbose_name="Date_debut")
    date_fin   = models.DateField(verbose_name="Date de fin")

    def __str__(self):
        date_debut_str = self.date_debut.strftime("%d/%m/%yy")
        date_fin_str = self.date_fin.strftime("%d/%m/%yy")
        return f"{date_debut_str}-- {date_fin_str}"
    
class Stag(models.Model):
    rapport_stage = models.ForeignKey(Rapport, related_name="rapport_stage", on_delete=models.CASCADE, null=True, blank=True)
    periode = models.ForeignKey(Periode, related_name="periode", on_delete=models.CASCADE, verbose_name="periode_stage")
    projet = models.ForeignKey(Projet, related_name="projet", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.projet}"