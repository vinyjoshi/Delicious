from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from booking.models import booking,Inquiry

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully Logged In!!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials!!')
            return redirect('login')
    else: 
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'Logout Successful!!')
        return redirect('home') 

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check Passwords matches: 
        if password == password2:
            # check if Username is taken or not:
            if User.objects.filter(username='username').exists():
                messages.error(request, 'Username already Taken!!')
                return redirect('register')
            else:
                # Check if e-mail already exists:
                if User.objects.filter(email='email').exists():
                    messages.error(request, "User is already registered with this mail id!!")
                    return redirect('register')
                else:
                    User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                        email=email, password=password).save()
                    messages.success(request, 'User Registered!!')
                    return redirect('login')
        else:
            messages.error(request, "Password doesnot Match!!")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def profile(request):
    bookings = booking.objects.order_by('date').filter(user_id=request.user.id)
    context = {
        'bookings' : bookings,
    }
    return render(request, 'accounts/dashboard.html', context)
