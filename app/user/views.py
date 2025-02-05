
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User, auth

# Create your views here.


def profile(request):
    return render(request, 'user/profile.html')

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
             user = User.objects.create_user(username=username, password=password1)
             user.save()
             return HttpResponseRedirect(reverse('user:login'))
    else:

        return render(request, 'user/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            

            return HttpResponseRedirect(reverse('main:index'))
       
    else:
       
        return render(request, 'user/login.html')

def logout(request):

    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


