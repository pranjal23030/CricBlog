from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as LOGIN
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create(
            username = username, 
            email = email, 
        )
        user.set_password(password)
        user.save()
        return redirect("login")
    return render(request,'auth/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            LOGIN(request, user)
            return redirect("home")
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid username or password'})
    return render(request, 'auth/login.html')

@login_required
def profile(request):
    return render(request, 'auth/profile.html', {'user': request.user})
