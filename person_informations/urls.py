from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('felicitation/', views.send_email, name='send_mail'),
]
