from django.urls import path    
from django.http import HttpResponseRedirect
from django.shortcuts import render
from auth import forms 
from django.contrib.auth import authenticate #this is for authenication in django 

def auth_login(request):
    loginform= forms.LoginForm()
    error= None
    
    if request.method == "POST":
        loginform=forms.LoginForm(request.POST)  #heck if the HTTP request method is "POST" before instantiating the loginform variable with data from the POST request. This is the standard way to handle forms in Django views when you want to process data submitted via a POST request.
        if loginform.is_valid():
            username=loginform.cleaned_data['username']  #this is used to do the filter sql injected data 
            password=loginform.cleaned_data['password']
            user=authenticate(username= username,password= password)
            if user:
                return HttpResponseRedirect('/')
            else:
                error="invalid usename or passwoed "
                
            
    context={"form":loginform,
             "error":error  
             }
    return render(request, 'auth/login.html', context)
    
