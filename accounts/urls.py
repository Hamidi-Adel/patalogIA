from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.accounts, name='signupPage'),
    path('login/',views.loginUser, name='loginPage'),
    path('logout/',views.logoutUser, name='logoutPage'),
]
