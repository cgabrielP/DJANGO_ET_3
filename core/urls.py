from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginV, name='login'),
    path('register', views.registerV, name='register'),
    path('product/<int:id>', views.prodDetail, name='prodDetail'),
]
