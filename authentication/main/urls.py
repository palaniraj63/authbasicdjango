from django.shortcuts import render
from main import views
from django.urls import path 
# Create your views here.
urlpatterns=[
   
    path('',views.index,name= 'index')
]