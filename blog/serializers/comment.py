from rest_framework import serializers
from ..models import User, Articulo, Comment
from .serializers import User2Serializer, Article2Serializer

class CommentSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=250)
    creation_date = serializers.DateTimeField()
    articulo = Article2Serializer()
    user = User2Serializer()
    
    
    def create(self, validated_data):
        content = validated_data.get("content")
        creation_date = validated_data.get("creation_date")
        validated_article =  validated_data.get("articulo")
        validated_user = validated_data.get("user")
        
        article_id = validated_article.get("id")
        try:
            articleId = Articulo.objects.get(id=article_id)
        except Articulo.DoesNotExist:
            raise serializers.ValidationError("Article with ID {} does not exist".format(article_id))   
        
        user_id = validated_user.get('id')
        try:
            userId = User.objects.get(id=user_id)
        
        except User.DoesNotExist:
            raise serializers.ValidationError("User whith Id {} does not exist".format(user_id))
        
        
        return Comment.objects.create(content=content, creation_date=creation_date, articulo=articleId, user=userId)
