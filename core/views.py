from django.shortcuts import render
from .models import Product
# Create your views here.
def home(req):
    products = Product.objects.all()
    return render(req, 'home.html', {'products': products})