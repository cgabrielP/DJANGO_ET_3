from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(req):
    products = Product.objects.all()
    return render(req, 'home/index.html', {'products': products})

def loginV(req):
    if req.method=='POST':
        username = req.POST['username']
        password = req.POST['pass']

        user=authenticate(req,username=username,password=password)

        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            messages={
                'error':'Credenciales invalidas'
            }
            return render(req,'login/index.html',messages)

    return render(req,'login/index.html') 

def logoutV(req):
    logout(req)
    return redirect('login')

def registerV(req):
    return render(req,'register/index.html')

def prodDetail(req,id):
    product = Product.objects.get(id=id)
    return render(req,'productDetail/index.html',{'product':product})