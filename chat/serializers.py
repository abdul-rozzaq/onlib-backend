from rest_framework.serializers import ModelSerializer

from library.serializers import UserSerializer

from .models import *


class GroupSerializer(ModelSerializer):
    owner = UserSerializer()
    members = UserSerializer(many=True)
    
    
    class Meta:
        model = Group
        fields = '__all__'


class MessageSerializer(ModelSerializer):
    sender = UserSerializer()
    
    class Meta:
        model = Message
        fields = '__all__'
        
    

    