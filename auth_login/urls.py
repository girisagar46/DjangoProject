from django.urls import path

from .views import loginForm, login_user, logout_user

urlpatterns = [
    path('login/', loginForm, name='login_form'),
    path('login-user/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout'),
]