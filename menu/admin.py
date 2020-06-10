from django.contrib import admin
from .models import menu, special

# Register your models here.

admin.site.register(special)

class menuAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'Tag','is_published','price')
    list_display_links = ('id','name')
    list_editable = ('is_published',)

admin.site.register(menu,menuAdmin )
