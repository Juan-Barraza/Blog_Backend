from rest_framework import  status
from rest_framework.response import Response
from ..serializers.comment import CommentSerializer 
from rest_framework.views import APIView
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class CommentView(APIView):
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
    