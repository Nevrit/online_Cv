from django.shortcuts import render
from .models import Information, ExpertiseLanguage, ExpertiseFramework

# Create your views here.
def index(request):
    person_informations = Information.objects.all()
    languages = ExpertiseLanguage.objects.all()
    framework = ExpertiseFramework.objects.all()
    context = {"person_informations" : person_informations, "languages" : languages, "framework":framework}
    return render(request, 'index/index.html', context)
