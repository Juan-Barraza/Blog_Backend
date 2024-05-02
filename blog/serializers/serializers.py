from rest_framework import serializers



class User2Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=50)
    role = serializers.CharField(max_length=20)
    
    def to_internal_value(self, data):
        return {
            'id': data.get("id")
        }
    
    def to_representation(self, instance):
        return {
            'username': instance.username,
            'role': instance.role
        }
    

class Category2Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=10)
    
    def to_internal_value(self, data):
        return {
            "id": data.get("id")
        }
        
    def to_representation(self, instance):
        return {
            'name': instance.name
        }
        

class Article2Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    
    def to_internal_value(self, data):
        return {
            "id": data.get("id"),
        }
        
    def to_representation(self, instance):
        return {
            'title': instance.title
        }
        
