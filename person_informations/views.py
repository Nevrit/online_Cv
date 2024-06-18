from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Information, ExpertiseLanguage, ExpertiseFramework, Portfolio, Contact, Resume, Service
from django.core.mail import send_mail, BadHeaderError
from settings import settings
from .forms import MessageForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from wkhtmltopdf.views import PDFTemplateResponse


def index(request):
    person_informations = Information.objects.all()
    languages = ExpertiseLanguage.objects.all()
    framework = ExpertiseFramework.objects.all()
    portfolios = Portfolio.objects.all()
    resume = Resume.objects.all()
    services = Service.objects.all()
    context = {"person_informations" : person_informations, "languages" : languages, "framework":framework, "portfolios":portfolios, "resume":resume, "services":services}
    return render(request, 'index/index.html', context)


def send_email(request):
    # if this is a POST request we need to process the form data
    form = MessageForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            contact = Contact()
            contact.firstname = form.cleaned_data['firstname']
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.subject = form.cleaned_data["subject"]
            contact.message = form.cleaned_data['message']
            contact.save()
            send_mail("Portfolio",contact.message,contact.email,[settings.EMAIL_HOST_USER], fail_silently=False)
            
    # if a GET (or any other method) we'll create a blank form
    else:
        print('Rien n\'est passé')
        form = MessageForm()
    return render(request, 'index/sent_form_page.html', {'form': form})

def create_pdf(request):
    person_informations = Information.objects.all()
    context = {'person_informations': person_informations}
    html = render_to_string('index/pdf.html', context)
    return PDFTemplateResponse(request=request,
                               template='index/pdf.html',
                               filename='mon_pdf.pdf',
                               context=context)