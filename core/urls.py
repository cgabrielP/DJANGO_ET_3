from django.urls import path
from .views import home,loginV,registerV,prodDetail,logoutV,customerData,pay

urlpatterns = [
    path('', home, name='home'),
    path('login', loginV, name='login'),
    path('logout', logoutV, name='logout'),
    path('register', registerV, name='register'),
    path('product/<int:id>', prodDetail, name='prodDetail'),
    path('customerData', customerData, name='customerData'),
    path('pay', pay, name='pay'),
]
