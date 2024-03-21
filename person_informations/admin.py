from django.contrib import admin
from .models import Information

# Register your models here.
class PersonnalInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "email", "phone_number", "position"]
    
admin.site.register(Information, PersonnalInfoAdmin)
