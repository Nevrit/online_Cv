from django.contrib import admin
from .models import Information, ExpertiseLanguage, ExpertiseFramework

class PersonnalInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "email", "phone_number", "position"]
    
class ExpertiseLanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "percentage_value"]
    

class ExpertiseFrameworkAdmin(admin.ModelAdmin):
    list_display = ["name", "percentage_value"]
    
    
admin.site.register(Information, PersonnalInfoAdmin)
admin.site.register(ExpertiseLanguage, ExpertiseLanguageAdmin)
admin.site.register(ExpertiseFramework, ExpertiseFrameworkAdmin)
