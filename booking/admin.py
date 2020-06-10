from django.contrib import admin
from .models import booking, Inquiry

# Register your models here.
class bookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','date', 'time', 'people')
    list_display_links = ('id', 'name')
    list_filter = ('date','time', 'people')
    
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')


admin.site.register(booking, bookAdmin)
admin.site.register(Inquiry, InquiryAdmin)
