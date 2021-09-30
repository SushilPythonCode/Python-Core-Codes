from django.shortcuts import render, HttpResponse,redirect
from .models import *

# Create your views here.
def index(request):
    product=Product.objects.all()
    cat=Category.objects.all()
    sub=Subcategory.objects.all
    # result=[product,cat,sub]
    return render(request,'table_relations/table.html',{'products': product, 'category':cat, 'subcategory':sub})
    # return render(request,'table_relations/table.html',{'res':result})