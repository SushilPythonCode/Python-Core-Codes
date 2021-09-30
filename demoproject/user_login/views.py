from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User #importing auth user
from django.contrib.auth.hashers import make_password #required for encrypt password
from django.contrib.auth import authenticate,login #required for authenticate user
from django.contrib.auth import get_user_model #required for auth user
User = get_user_model() #required for auth user
from django.contrib import messages
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.conf import settings



# Create your views here.
def index(request):
        
    return render(request,'home/index.html')
 
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
 
       
        user=User.objects.create(first_name=first_name,last_name=last_name,email=email,password=make_password(password),username=username)
        user.save();
        return redirect('login')


    return render(request,'home/register.html')

def login_view(request):

    if request.method=='POST':
        username1=request.POST.get('username')
        password2=request.POST.get('password')
        user =authenticate(username=username1, password=password2)
        
        # if username1 =="":
        #    messages.info(request,' Username cannot be blank')
          
        #    return render(request, 'login', {'message':messages})

        if user is not None:
            login(request, user)
            context={'user':user}
            # return render(request, 'home/dashboard.html')
            return redirect('dashboard')
        # else:
        #     messages.info(request,' You! have entered wrong credentials')
        #     return redirect('login')
    return render(request,'home/login.html')


# @login_required()
def dashboard(request):
    blog=Blog.objects.all()

    return render(request, 'home/dashboard.html',{'blog':blog,
    'media_url':settings.MEDIA_URL} )
# @login_required()
# @login_required(redirect_field_name='login')
def blog(request):
    if request.method=='POST':

       heading=request.POST.get('heading')
       description=request.POST.get('description')
       contents=request.POST.get('content')
       image=request.FILES.get('image')
       a=Blog.objects.create(heading=heading,description=description,
                            Content=contents,image=image, author_id = request.user.id)
       a.save();
       return redirect('dashboard')
    return render(request, 'home/addblog.html' )

# @login_required()
def blog_view(request):

    blog=Blog.objects.filter(author_id=request.user.id)

    return render(request, 'home/myblogs.html',{'blog':blog,
    'media_url':settings.MEDIA_URL} )
   

def delete_blog(request,id):
    # id=request.GET.get('id')
    deleteblog=Blog.objects.get(id = id,author_id=request.user.id)
    # delete id from blog where id = id and author_id = request krne wale user ki id
    # print(deleteblog.query,">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    if deleteblog:
        deleteblog.delete()
        return redirect('myblog')
