from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login #required for authenticate user
from django.db.models import Q




class Index(View):
    
    def get(self,request):
        return render(request,'index.html')


class Registration(View):

    def post(self,request):
        if request.method=='POST':

            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
        
        register=User.objects.create(first_name=fname,last_name=lname, email=email,
         username=username, password=make_password(password))
        register.save();
        return redirect("crud_application:login")

    
 
class LoginStudent(View):
    
    
    def get(self, request,*args ,**kwargs):
        return render(request, 'login.html')
    
    def post(self,request, *args ,**kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = User.objects.get(Q(username = username) | Q(email =username))
        if user:
           authenticate(username=user.username, password=user.password)
      
           if user is not None:
                login(request, user)
            
                return redirect('crud_application:dashboard')

class Dashbaord(View):

    def get(self,request):
        user=User.objects.all()

        return render(request, 'dashboard.html',{'user':user})


class EditView(View):

    def get(self,request,id):
        student_detail=User.objects.get(id=id)
    
        return render(request, 'edit.html', {'details':student_detail})

    
    def post(self,request):

        userupdate=User.objects.get(id=request.POST.get('id'))
        if userupdate:
            userupdate.first_name = request.POST.get("fname")
            userupdate.last_name = request.POST.get("lname")
            userupdate.email = request.POST.get("email")
            userupdate.username = request.POST.get("username")
        
            userupdate.save()
            return redirect('crud_application:dashboard')


def delete(request,id):
        
    DeleteStudent=User.objects.get(id=id)
        
    DeleteStudent.delete()
    return redirect('crud_application:dashboard')
    





