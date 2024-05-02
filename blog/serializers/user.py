from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=128)
    email = serializers.EmailField(max_length=30)
    role = serializers.CharField(max_length=20)
    
    
    def create(self, validated_data):
        username = validated_data.get('name')
        password = validated_data.get('password')
        email = validated_data.get('email')
        role = validated_data.get('role')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("the User already exists")
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user