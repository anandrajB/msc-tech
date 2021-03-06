from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.http import HttpResponse
from django.template import loader
from .models import Names , Spares
from django.contrib.auth.models import User as user



@csrf_exempt
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('/table')
        else: 
            messages.info(request, 'Invalid Username or Password')
            return redirect('/')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('')



def home(request):
    data = Spares.objects.filter( username = "karthick" , states = "GUIDE").values()
    print(data)
    context = {
    'data': data
    }
    return render(request,'index.html',context)

def overview(request):
    data = Spares.objects.filter( username = "karthick" ).values()
    context = {
    'data': data
    }
    return render(request,'overview.html',context)


def home2(request):
    data = Spares.objects.filter( username = "karthick" ,states = "EXPERT").values()
    print(data)
    context = {
    'data': data
    }
    return render(request,'index2.html',context)



def table(request):
    # user = request.user
    data = user.objects.exclude(is_superuser = True).values()
    context = {
    'data': data
    }
    return render(request,'table.html',context)





def piston(request):
    mydata = Names.objects.filter(title = 'PISTON',user = request.user.id)
    template = loader.get_template('piston.html')
    context = {
    'mymembers': mydata
    }
    print(context)
    return HttpResponse(template.render(context, request))



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
    data = Spares.objects.filter(username = "karthick" ).values()
    context = {
    'data': data
    }
    return render(request,'mode.html',context)



