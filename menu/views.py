from django.shortcuts import render
from .models import menu, special
from chefs.models import chef
from booking.choices import *

# Create your views here.
def Menu(request):
    chefs = chef.objects.order_by('id')
    menuItem = menu.objects.all()
    specialItem = special.objects.order_by('id')
    context = {
        'chefs' : chefs,
        'menuItem' : menuItem,
        'specialItem' : specialItem,
        'Date' : Date,
        'Month' : Month,
        'Hour' : Hour,
        'Minutes' : Minutes, 
        'when' : when,
    }
    return render(request, 'menu/menu.html', context)
