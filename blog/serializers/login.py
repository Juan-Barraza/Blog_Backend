from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist  
from ..models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=11)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            try:
                user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                raise serializers.ValidationError("Email or password incorrect")
            print("data", data)
            return data 
        else:
            raise serializers.ValidationError("Both email and password are required.")
