from django.shortcuts import render
from .models import Information

# Create your views here.
def index(request):
    person_informations = Information.objects.all()
    context = {"person_informations" : person_informations}
    return render(request, 'index/index.html', context)
