from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length= 11)
    role = serializers.CharField(max_length=20)
    
    
    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        password = validated_data.get('password')
        role = validated_data.get('role')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("the User already exists")
        
        return User.objects.create(**validated_data)
    