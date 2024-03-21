from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Information(models.Model):
    
    BAC = "BAC"
    BTS = "BAC+2"
    LICENSE = "BAC+3"
    MASTER = "BAC+5"
    DOCTORAT = "BAC+8"
    DEGREE_YEAR = {
        BAC: "Baccalauréat",
        BTS: "Brevet de Technicien Supérieur",
        LICENSE: "license",
        MASTER: "master",
        DOCTORAT: "doctorat",
    }
    
    name = models.CharField(max_length = 50, verbose_name="Nom")
    last_name = models.CharField(max_length=150, verbose_name="Prénom")
    birthdate = models.DateField(verbose_name="Date d'anniversaire")
    email = models.EmailField(verbose_name="Email")
    phone_number = PhoneNumberField(blank=False, verbose_name="Numéro de téléphone") 
    address = models.CharField(max_length=100, verbose_name="Adresse")
    degree = models.CharField(
        max_length=50,
        choices=DEGREE_YEAR.items(),
        default=BAC,
    )
    year_of_graduation = models.DateField(verbose_name="Date de l'obtention du diplôme")
    institution = models.CharField(verbose_name="Nom de l'école", max_length=100)
    position = models.CharField(max_length=100, verbose_name="Titre du poste occupé")
    company = models.CharField(max_length=100, verbose_name="Nom de la société")
    hiring_date = models.DateField(verbose_name="Date d'embauche")
    
    def __str__(self):
        return self.name
