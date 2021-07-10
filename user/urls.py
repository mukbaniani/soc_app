from django.contrib.auth import views as auth_view
from django.urls import path
from . import views

urlpatterns = [ 
    path('login/', auth_view.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('', views.Register.as_view(), name='register')
]