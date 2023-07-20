from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


from library.models import *
from library.serializers import *



class ListCategories(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

    def get(self, request, format=None):
        """
        Return a list of all categories.
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data
        
        serializer = CategorySerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            data = {
                'status': True,
                'message': 'Category was successfully created'
            }
            
            return Response(data)

        else:
            return Response(serializer.errors)
            
    
        
        
class ListAuthors(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer
    
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        print(request.data)
        
        return Response({'status': 200})


class ListBooks(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = BookSerializer 
    
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        
    
    def post(self, request, format=None):
        user: User = request.user
        data = request.data
        
        if user.is_staff:
            
            serializers = BookSerializer(data=data)
            
            if serializers.is_valid():
                serializers.save()
                
                return Response({'status:' : 201}, status=201)
            
            else:
                return Response(serializers.errors)
        else:
            return Response({'status': 403}, status=403)

    
    
    
    