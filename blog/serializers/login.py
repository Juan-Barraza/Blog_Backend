from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:        
            return data 
        else:
            raise serializers.ValidationError("Both email and password are required.")
