from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User #importing auth user
# from django.contrib.auth.hashers import make_password #required for encrypt password
# from django.contrib.auth import authenticate #required for authenticate user
# from django.contrib.auth import get_user_model #required for auth user
# User = get_user_model() #required for auth user


# Create your views here.
#Authenticating without using auth user
def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password=request.POST['pass']
        state=request.POST['state']


        user=User.objects.create(state=state,username=username, password=make_password(password), first_name=first_name, last_name=last_name)
        user.save();
        return redirect('auth_login')


    return render(request,'auth_login/register.html')

def login(request):

    if request.method=='POST':
        username1=request.POST.get('username')
        password2=request.POST.get('pass')
        user =authenticate(username=username1, password=password2)
       
        if user is not None:
            return render(request,'auth_login/dashboard.html')
        else:
            return render(request,'auth_login/login.html')
    return render(request,'auth_login/login.html')

def dashboard(request):
    return render(request, 'auth_login/dashboard.html')