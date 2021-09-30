from django import http
from django.http.response import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q
from django.contrib.auth.models import User #importing auth user
from django.contrib.auth.hashers import make_password #required for encrypt password
from django.contrib.auth import authenticate,login #required for authenticate user
from django.contrib.auth import get_user_model #required for auth user
User = get_user_model() #required for auth user
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Count    






class IndexView(View):
    def get(self , request ,*args ,**kwargs):
        return render(request , 'admin/index.html')

class Register(View):
   
    def get(self, request):
        return render(request, 'login_register/register.html')

    def post(self,request, *args ,**kwargs):
        #  if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        username=request.POST['username']

        mobile_no=request.POST['mobile']
 
       
        user=User.objects.create(first_name=first_name,last_name=last_name,email=email,usertype=5,
        password=make_password(password1),password2=make_password(password2),mobile_no=mobile_no,username=username  )
        user.save();
        return redirect('/login')

class Login(View):
   
    def get(self, request,*args ,**kwargs):
        return render(request, 'login_register/login.html')
    
    def post(self,request, *args ,**kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = User.objects.get(Q(username = username) | Q(email =username) | Q(mobile_no = username))
        if user:
           authenticate(username=user.username, password=user.password)
      
           if user is not None:
                login(request, user)
            
                return redirect('/dashboard')
                # return render(request, 'login_register/dashboard.html')    

 
class dashboard(View):
    
    # @method_decorator(login_required, name='dispatch')


    def get(self, request, *args ,**kwargs):

        if request.user.is_authenticated== True and request.user.is_superuser == False and request.user.usertype== 5:
            user=User.objects.all()
            user_count=user.count()
            context={'user':user,
                    'user_count':user_count
                    }
            return render(request, 'login_register/dashboard.html', context)
        
       
        elif request.user.is_authenticated==True and request.user.is_superuser ==True and request.user.usertype==1:
            user=User.objects.all()
            user_count=user.count()
            context={'user':user,
                    'user_count':user_count
                    }
            # return render(request, 'login_register/dashboard.html', context)
            return HttpResponse("Admin View")
        
        elif request.user.is_authenticated==True and request.user.is_superuser ==False and request.user.usertype==2:
            user=User.objects.all()
            user_count=user.count()
            context={'user':user,
                    'user_count':user_count
                    }
            # return render(request, 'login_register/gm_dashboard.html', context)
            return HttpResponse('General Manager view')

class edit(View):

        def get(self, request, id):
            display=User.objects.get(id=id) 
    
            if display:
                return render(request, 'login_register/edit.html',{'detail' : display})
            else:
                return redirect('/dashboard')


class updateuser(View):

    def post(self, request, *args,**kwargs):    
        userupdate=User.objects.get(id=request.POST.get('id'))
        if userupdate:
            userupdate.first_name = request.POST.get("first_name")
            userupdate.last_name = request.POST.get("last_name")
            userupdate.email = request.POST.get("email")
            userupdate.username = request.POST.get("username")
            userupdate.mobile_no = request.POST.get("mobile_no")
        
            userupdate.save()
            return redirect('/dashboard')
        return render(request, 'login_register:register.html')

class delete(View):
    def get(self, request, id):

        deleteuser=User.objects.get(id=id)
        if deleteuser:
           deleteuser.delete()
           return redirect('/dashboard')



class contact(View):
    def get(self, request, *args ,**kwargs):
        return render(request, 'login_register/contact.html')

class about(View):
   
    def get(self, request, *args ,**kwargs):
        return render(request, 'login_register/about.html')


#Gm page--------------------------------------------------------
class Gm_list(View):
    def get(self, request, *args ,**kwargs):
        return render(request, 'admin/GM/gmlisting.html')
        
class Gm_view(View):
    def get(self, request, *args ,**kwargs):
        return render(request, 'admin/GM/gmcredentials.html')

    def post(self,request, *args ,**kwargs):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']   
        username=request.POST['username']

        mobile_no=request.POST['mobile_no']
 
       
        user=User.objects.create(first_name=first_name,last_name=last_name,email=email,
        password=make_password(password),mobile_no=mobile_no,username=username, is_superuser=0,usertype=2)
        user.save();
        return redirect('login_register:gmlist')