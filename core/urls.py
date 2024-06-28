from django.urls import path
from .views import home,loginV,registerV,prodDetail,customerData

urlpatterns = [
    path('', home, name='home'),
    path('login', loginV, name='login'),
    path('register', registerV, name='register'),
    path('product/<int:id>', prodDetail, name='prodDetail'),
    path('customerData', customerData, name='customerData'),
]
