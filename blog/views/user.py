from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.user import UserSerializer



class UserView(APIView):
    
    def post(self, request):
        
        try: 
            serializer = UserSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        except ValueError as a:
            return a