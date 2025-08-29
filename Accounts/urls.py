from django.urls import path
from .views import register_user, login_user
from . import views 


# app_name = "Accounts"

urlpatterns = [
    path('account/register', register_user, name='register_user'),
    path('account/login', login_user, name='login_user')
]