from django.shortcuts import render
from .models import Information, ExpertiseLanguage, ExpertiseFramework, Portfolio

# Create your views here.
def index(request):
    person_informations = Information.objects.all()
    languages = ExpertiseLanguage.objects.all()
    framework = ExpertiseFramework.objects.all()
    portfolios = Portfolio.objects.all()
    context = {"person_informations" : person_informations, "languages" : languages, "framework":framework, "portfolios":portfolios}
    return render(request, 'index/index.html', context)
