from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate



# Create your views here.
#Authenticating without using auth user
def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password=request.POST['pass']

        user=User.objects.create(username=username, password=make_password(password), first_name=first_name, last_name=last_name)
        user.save();
        return redirect('login')


    return render(request,'custom_user/register.html')

def login(request):

    if request.method=='POST':
        username1=request.POST.get('username')
        password2=request.POST.get('pass')
        user =authenticate(username=username1, password=password2)
       
        if user is not None:
            return render(request,'custom_user/dashboard.html')
        else:
            return render(request,'custom_user/login.html')
    return render(request,'custom_user/login.html')

def dashboard(request):
    return render(request, 'custom_user/dashboard.html')