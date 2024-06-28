from django.urls import path
from .views import home,loginV,registerV,prodDetail,logoutV

urlpatterns = [
    path('', home, name='home'),
    path('login', loginV, name='login'),
    path('logout', logoutV, name='logout'),
    path('register', registerV, name='register'),
    path('product/<int:id>', prodDetail, name='prodDetail'),
]
