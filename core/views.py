import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from .models import Product,Order,OrderDetail
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    if req.method=='POST':
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        email = req.POST['email']
        username=email.split('@')[0] 
        password = req.POST['pass']
        user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        if user is not None:
            return redirect('login')
        else:
            messages={
                'error':'Datos invalidos'
            }
            return render(req,'register/index.html',messages)
        
    return render(req,'register/index.html')

def prodDetail(req,id):
    product = Product.objects.get(id=id)
    return render(req,'productDetail/index.html',{'product':product})

@login_required
def customerData(req):
    user = req.user
    return render(req,'customerData/index.html',{'user' : user})

def pay(req):
    return render(req, 'pay/index.html')

@login_required
def edit_user(req):
    if req.method == 'POST':
        method = req.POST.get('_method', '').upper()
        if method == 'PUT':
            user = req.user
            user.username = req.POST.get('username')
            user.first_name = req.POST.get('first_name')
            user.last_name = req.POST.get('last_name')
            user.email = req.POST.get('email')
            user.save()
            return redirect('customerData')  
    return render(req, 'edit_user.html')

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
        redirect('home')
    return render(request, 'confirmDelete/index.html')
    

@csrf_exempt
@login_required
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            products = data.get('products', [])
            
            # Crear la orden
            order = Order.objects.create(user=request.user, status='Pending', total_amount=0.00)

            total_amount = 0
            for item in products:
                product = Product.objects.get(id=item['id'])
                quantity = item['quantity']
                price = product.price

                OrderDetail.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )

                total_amount += quantity * price

            order.total_amount = total_amount
            order.save()
            redirect('home')
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})