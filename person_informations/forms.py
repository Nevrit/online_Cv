from django import forms
from .models import Form


class MessageForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['first_name', 'name', 'email', 'subject', 'message']