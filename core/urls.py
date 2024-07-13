from django.urls import path
from .views import home,loginV,registerV,prodDetail,logoutV,customerData,pay,edit_user,delete_user,create_order

urlpatterns = [
    path('', home, name='home'),
    path('login', loginV, name='login'),
    path('logout', logoutV, name='logout'),
    path('register', registerV, name='register'),
    path('product/<int:id>', prodDetail, name='prodDetail'),
    path('customerData', customerData, name='customerData'),
    path('pay', pay, name='pay'),
    path('edit_user', edit_user, name='edit_user'),
    path('delete_user', delete_user, name='delete_user'),
    path('create_order/', create_order, name='create_order'),
]
