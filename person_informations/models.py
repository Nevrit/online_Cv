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
    image = models.ImageField(upload_to='pics_on_myself/', height_field=None, width_field=None, max_length=100,)
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
    
    
    class Meta:
        verbose_name = 'Information Personnelles'
        
    def __str__(self):
        return self.name
    
# Langague do you know  
class ExpertiseLanguage(models.Model):
    
    name = models.CharField(max_length=30, verbose_name="Nom du langage")
    icon = models.CharField(max_length=50, verbose_name="Classe de l'icône FontAwesome")
    percentage_value = models.IntegerField(default=0, choices=((i,i) for i in range(0, 101)), verbose_name="Niveau de connaisance")

    
    class Meta:
        verbose_name = 'Langage Informatique'
        verbose_name_plural = 'Langage Informatique'
        
    def __str__(self):
        return self.name

# Framework do you know  
class ExpertiseFramework(models.Model):
    
    name = models.CharField(max_length=30, verbose_name="Nom du langage")
    icon = models.CharField(max_length=50, verbose_name="Classe de l'icône FontAwesome")
    percentage_value = models.IntegerField(default=0, choices=((i,i) for i in range(0, 101)), verbose_name="Niveau de connaisance")
    
