from django.urls import path
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.home, name='StartPage'),
    path('aboutus/', views.aboutus, name='aboutUs'),
]
