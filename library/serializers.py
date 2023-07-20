from rest_framework import serializers
from rest_framework.validators import ValidationError
from library.models import *

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name',] 
        
    def validate_name(self, name):
        if Category.objects.filter(name=name).exists():
            raise ValidationError({'message' : f'{name} category already exists'})
        
        else:
            return name



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'