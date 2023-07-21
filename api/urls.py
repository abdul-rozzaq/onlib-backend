from django.urls import path

from api.views import *

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('categories/', ListCategories.as_view()),
    path('authors/', ListAuthors.as_view()), 
    path('books/', ListBooks.as_view()), 
        
    path('login/', obtain_auth_token, name='login'),
    path('register/', register_user, name='register'),
    
    path('user/', check_auth_token, name='user'),
    
]

