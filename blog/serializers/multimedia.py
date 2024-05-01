from rest_framework import serializers
from ..models import Articulo, Multimedia
#from .serializers import Article2Serializer


class MultimediaSerializer(serializers.ModelSerializer):
    # archivo = serializers.FileField()
    # description = serializers.CharField(max_length=50)
    # articulo = Article2Serializer()
    
    # def create(self, validated_data):
    #     archivo = validated_data.get('archivo')
    #     print(archivo)
    #     description = validated_data.get('description')
    #     article = validated_data.get('articulo')
    #     article_id = article.get('id')
    #     try:
    #         articleId = Articulo.objects.get(id=article_id)
    #     except Articulo.DoesNotExist:
    #         raise serializers.ValidationError("Article with ID {} does not exist".format(article_id))
        
    #     return Multimedia.objects.create(archivo=archivo, description=description, articulo=articleId)
           
    class Meta:
        model = Multimedia
        fields = "__all__"
        