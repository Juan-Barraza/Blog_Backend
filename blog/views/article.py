from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import  status
from rest_framework.response import Response
from ..serializers.article import ArticleSerializer
from rest_framework.views import APIView


@permission_classes([IsAuthenticated])
class ArticleView(APIView):
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)   
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
