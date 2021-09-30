from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from django.contrib import auth #authm
from django.contrib.auth.hashers import make_password




def register(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass']

        user=User.objects.create(username=username, password=make_password(password), email=email, first_name=first_name, last_name=last_name)
        user.save();
        return redirect('auth')
        # return render(request,'auth/login.html')


    return render(request,'auth/auth.html')




def login(request):

    if request.method=='POST':
        username1=request.POST.get('uname')
        password2=request.POST.get('password')
        print(username1,password2)
        user =authenticate(username=username1, password=password2)
       
        if user is not None:
            return render(request,'logedin.html')
        else:
            return render(request,'auth/auth.html')
    return render(request,'auth/login.html')
#     #  
#     # x=auth.authenticate(username=username1, password=password2)
        
#     # if x is None:
#     #    return redirect ('login')
#     # else:
#     #     return render(request,'auth/auth.html')
 
#         #     auth.login(request, user)
#         #     return render(request,'auth/auth.html')
#         # else:
#         #     return render(request,'auth/dashboard.html')
            
#     # return render(request,'auth/login.html')


# def dashboard(request):
#     return render(request,'auth/dashboard.html')


# def test(request):
#     if request.method=='POST':
#        username=request.POST['username']
#        password=request.POST['password']

#        x=auth.authenticate(username=username, password=password)
#        if x is None:
#          return HttpResponse('test')
#        else:
#          return HttpResponse('auth')
#     return render(request, 'auth/test.html')