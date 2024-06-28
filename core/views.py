from django.shortcuts import render
from .models import Product
# Create your views here.
def home(req):
    products = Product.objects.all()
    return render(req, 'home/index.html', {'products': products})

def loginV(req):
    return render(req,'login/index.html') 

def registerV(req):
    return render(req,'register/index.html')

def prodDetail(req,id):
    product = Product.objects.get(id=id)
    return render(req,'productDetail/index.html',{'product':product})

def customerData(req):
    return render(req,'customerData/index.html')