from django.urls import path    
from auth import views


urlpatterns=[
   
    path('login/',views.auth_login,name= 'auth_login')
]
