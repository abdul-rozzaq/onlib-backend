from django.urls import path

from api.views import *


urlpatterns = [
    path('categories/', ListCategories.as_view()),
    path('authors/', ListAuthors.as_view()), 
    path('books/', ListBooks.as_view()), 
]