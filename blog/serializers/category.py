from rest_framework import serializers
from ..models import Category


class CategorySerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=50)
    
    
    def create(self, validated_data):
        name = validated_data.get('name')
        description = validated_data.get('description')
        
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError("the category already exists")
    
        return Category.objects.create(**validated_data)


    def get(self, validated_data):
        name = validated_data.get('name')   
        description = validated_data.get('description') 
        if name: 
            return Category.objects.filter(name=name, description=description)
    
        return Category.objects.all()

