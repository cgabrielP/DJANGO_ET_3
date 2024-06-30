from django.urls import path
from .views import home,loginV,registerV,prodDetail,logoutV,customerData,edit_user,delete_user

urlpatterns = [
    path('', home, name='home'),
    path('login', loginV, name='login'),
    path('logout', logoutV, name='logout'),
    path('register', registerV, name='register'),
    path('product/<int:id>', prodDetail, name='prodDetail'),
    path('customerData', customerData, name='customerData'),
    path('edit_user', edit_user, name='edit_user'),
    path('delete_user', delete_user, name='delete_user'),
]
