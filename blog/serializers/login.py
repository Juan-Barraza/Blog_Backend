from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from ..models import User

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length= 11)
    
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = User.objects.get(email=email)
            if user is None:
                raise serializers.ValidationError("email  incorrect")
            
            if not check_password(password, user.password):
                raise serializers.ValidationError("password incorrect")
            
            return data
        else:
            raise serializers.ValidationError("Both email and password are required.")
