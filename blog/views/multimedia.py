from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import  status
from rest_framework.response import Response
from ..serializers.multimedia import  MultimediaSerializer
from rest_framework.views import APIView
from ..models import Multimedia



@permission_classes([IsAuthenticated])
class MultimediaView(APIView):
    
    def get(self, request):
        multimedia = Multimedia.objects.all()
        serializer = MultimediaSerializer(multimedia, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MultimediaSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)