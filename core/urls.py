from django.urls import path
from .views import home,loginV,registerV

urlpatterns = [
    path('', home, name='home'),
    path('login', loginV, name='login'),
    path('register', registerV, name='register'),
]
