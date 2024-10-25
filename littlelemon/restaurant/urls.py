from django.urls import path
from django.contrib import admin 
from .views import index, home
  
urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', index, name='index'),
    path('', home, name='home')
]