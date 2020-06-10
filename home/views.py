from django.shortcuts import render
from booking.choices import *

# Create your views here.
def index(request):
    context = {
        'Date' : Date,
        'Month' : Month,
        'Hour' : Hour,
        'Minutes' : Minutes, 
        'when' : when,
    }
    return render(request, 'home/index.html', context)

