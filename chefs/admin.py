from django.contrib import admin
from .models import chef

# Register your models here.
class chefDisplay(admin.ModelAdmin):
    list_display = ('id','name','designation','phone','city')
    list_display_links = ('id','name')
    list_filter = ('designation','join_date')
    search_fields = ('name','address','email','phone')
    
admin.site.register(chef, chefDisplay)