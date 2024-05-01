from rest_framework import serializers
from ..models import Category, User, Articulo
from .serializers import Category2Serializer, User2Serializer


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=255)
    publication_date = serializers.DateTimeField()
    autor = User2Serializer()
    category = Category2Serializer()
    
    def validate_title(self, value):

        if not value.strip():
            raise serializers.ValidationError("the title can not be empty.")
        return value
    
    
    def create(self, validated_data):
        title = validated_data.get('title')
        content = validated_data.get('content')
        publication_date = validated_data.get('publication_date')
        validated_autor = validated_data.get('autor')
        validated_category = validated_data.get('category')
        
        if Articulo.objects.filter(title=title).exists():
            raise serializers.ValidationError("the title already exists")
        
        autor_id = validated_autor.get('id')
        try:
            autorId = User.objects.get(id=autor_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with ID {} does not exist".format(autor_id))

        category_id = validated_category.get('id')
        try:
            categoryId = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with ID {} does not exist".format(category_id))
         
        return Articulo.objects.create(title=title,content=content, publication_date=publication_date, autor=autorId, category=categoryId)

           
    