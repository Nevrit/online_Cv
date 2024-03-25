from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Personal informations
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
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Information Personnelles'
        
    def __str__(self):
        return self.name
    
# Langague do you know  
class ExpertiseLanguage(models.Model):
    
    name = models.CharField(max_length=30, verbose_name="Nom du langage")
    icon = models.CharField(max_length=50, verbose_name="Classe de l'icône FontAwesome")
    percentage_value = models.IntegerField(default=0, choices=((i,i) for i in range(0, 101)), verbose_name="Niveau de connaisance")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
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
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Framework'
    

# Portfolio
class Portfolio(models.Model):
    card_image = models.ImageField(upload_to='portfolio/', height_field=None, width_field=None, max_length=100, verbose_name="Image de la card")
    card_title = models.CharField(max_length=50, verbose_name="Titre")
    description = models.TextField(max_length=300, verbose_name="Description")
    href = models.CharField(max_length=50, verbose_name="Le lien", help_text="Le lien que vous mettrez ici devra être le même que le id")
    id = models.CharField(max_length=50, verbose_name="id", help_text="Le id que vous mettrez ici devra être unique", unique=True, primary_key=True)
    aria_labelledby = models.CharField(max_length=100, verbose_name="aria-labelledby", editable=False, blank=True)
    carousel_image = models.ImageField(upload_to="carousel_portfolio_images/", height_field=None, width_field=None, max_length=100, verbose_name="images de la carousselle")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Portfolio'
    
    # This fonction allow to add "Label" at the end of the id
    def save(self, *args, **kwargs):
        self.aria_labelledby = f"{self.id}Label"
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.card_title
    
class CarouselPortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=False,upload_to='galery/', verbose_name='Image')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Carousel image'
        
class Contact(models.Model):
    firstname = models.CharField(blank=False, max_length=100, verbose_name='Prénom',)
    name = models.CharField(blank=False, max_length=100, verbose_name='Nom',)
    email = models.EmailField(blank=False, help_text='Veuillez entrer une adresse mail valide s\'il vous plaît', verbose_name='Email',)
    subject = models.CharField(blank=False, verbose_name='Objet', max_length=255)
    message = models.TextField(blank=True, max_length=5000, verbose_name='Message',)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Demande des client'