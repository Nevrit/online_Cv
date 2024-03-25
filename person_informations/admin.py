from django.contrib import admin
from .models import Information, ExpertiseLanguage, ExpertiseFramework, Portfolio, CarouselPortfolioImage, Contact

class PersonnalInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name", "email", "phone_number", "position", "create_at", "update_at"]
    
class ExpertiseLanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "percentage_value", "create_at", "update_at"]
    

class ExpertiseFrameworkAdmin(admin.ModelAdmin):
    list_display = ["name", "percentage_value", "create_at", "update_at"]

class ImageActualiteInline(admin.TabularInline):
    model = CarouselPortfolioImage
    readonly_fields = ('id',)
    extra = 2
    show_change_link = True

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ["card_title", "create_at", "update_at"]
    inlines = [ImageActualiteInline]
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ["firstname", "name", "email", "create_at", "update_at"]
    
admin.site.register(Information, PersonnalInfoAdmin)
admin.site.register(ExpertiseLanguage, ExpertiseLanguageAdmin)
admin.site.register(ExpertiseFramework, ExpertiseFrameworkAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Contact, ContactAdmin)

