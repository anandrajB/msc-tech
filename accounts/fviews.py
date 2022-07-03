from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

@csrf_exempt
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/selectmode')
        else: 
            messages.info(request, 'Invalid Username or Password')
            return redirect('/')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('')



def home(request):
    return render(request,'index.html')



def profile(request):
    return render(request,'profile.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create(username=username, password=password, 
                                        email=email)
                user.save()
                
                return redirect('/')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            
    else:
        return render(request, 'register.html')


def mode(request):
    return render(request,'mode.html')