from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Category
from ..serializers.category import CategorySerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class CategoryView(APIView):

    def get(self, request):

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
             
        if category is None:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        
    
        
        