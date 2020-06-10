from django.shortcuts import render, redirect
from .models import booking,Inquiry
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST.get('date', False) 
        month = request.POST.get('month', False) 
        Hour = request.POST.get('Hour', False) 
        Minutes = request.POST.get('Minutes', False) 
        when = request.POST.get('when', False)
        people = request.POST['people']
        user_id = request.POST['user_id']
    
        booking.objects.create(name=name, email=email, phone=phone, date=date+" "+month,time=Hour + ":" +  Minutes + when,
                               people=people, user_id=user_id).save()
        
        # Alert:
        messages.success(request, 'Booking Successful!')
        
        # Mail;
        send_mail(
            'Table booking at Delicious',
            'This is to inform you that your booking has been accepted at Delicious. We,ll be waiting for your arrival.\n\n Thanks and Regards.',
            'viyj1995@gmail.com',
            [email, 'viyj2000@gmail.com'],
            fail_silently = False,           
        )
        
        return redirect('/'+"#book-a-table")
    
    
def inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']
    
        Inquiry.objects.create(name=name, email=email, subject=subject, message=message,user_id=user_id).save()
        
        # Alert:
        messages.success(request, 'We\'ll get back to you as soon as possible!!')
        
        # Mail;
        send_mail(
            'Table booking at Delicious',
            'This is to inform you that your Inquiry has been Submitted to Delicious. We,ll get back back to you as soon as possible.\n\n Thanks and Regards.',
            'viyj1995@gmail.com',
            [email, 'viyj2000@gmail.com'],
            fail_silently = False     
        )
        
        return redirect('/'+"#contact")