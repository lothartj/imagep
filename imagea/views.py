from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from .models import Register
from django.contrib import messages
# Create your views here.
def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('password')
        password = request.POST.get('password')

        user = Register(username=username,email=email,password=password)    
        user.save()

        return redirect('user_home')
    
    return render(request, 'imagea/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, 'Username or password is incorrect')

     
    return render(request, 'imagea/login.html')


def user_home(request):
    return render(request, 'imagea/home.html')

