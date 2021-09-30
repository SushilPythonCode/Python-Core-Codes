from django.shortcuts import render
from .models import UserRegister

# Create your views here.

def index(request):

    user= UserRegister()
    user.fname="First name"
    user.lname="Last name"
    user.email= "Email"
    user.comment= "Comment"
    return render(request, 'index.html', {'user': user})
   # return HttpResponse("this is home page")   

