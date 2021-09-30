from django.shortcuts import render, HttpResponse,redirect
from .models import Test , Register #alternate way to call all models *



# Create your views here.
def index(request):
    users=Register.objects.all()

    return render(request, 'home.html', {'userdetail': users})
   # return HttpResponse("this is home page")   

def add(request):
    
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, 'result.html', {'result': res})
    

def register(request):
    if request.method=='POST':  
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        comment=request.POST['comment']
        username=request.POST['username']
        password=request.POST['password']

        user=Register.objects.create(first_name=first_name, last_name=last_name, email=email, comment=comment,password=password, username=username)
        user.save();
        
        return redirect('first_app:first_app')

    else:
        return render(request, 'register.html')    

def edit(request,id):
    display=Register.objects.get(id=id) 
    
    if display:
        return render(request, 'edit.html',{'detail' : display})
    else:
        return redirect('first_app')


def updateuser(request,id):
    updateuser=Register.objects.get(id=id)
    

    updateuser.first_name = request.POST.get("first_name")
    updateuser.last_name = request.POST.get("last_name")
    updateuser.email = request.POST.get("email")
    updateuser.username = request.POST.get("username")
    updateuser.password = request.POST.get("password")
    updateuser.comment = request.POST.get("comment")
    
    updateuser.save()

    return redirect('first_app:first_app')

def delete(request,id):
    
    deleteuser=Register.objects.get(id=id)
    if deleteuser:
        deleteuser.delete()
            
    # deleteeuser.delete()
    # deleteeuser.objects.filter(id=id).delete()


    
    return redirect('first_app:first_app')


# def about(request):
#     user=Test.objects.all()

#     return render(request, 'home.html', {'users': user})




