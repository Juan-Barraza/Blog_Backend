from rest_framework import  status
from rest_framework.response import Response
from ..serializers.login import LoginSerializer 
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class LoginView(APIView):
    
     def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(request=request, email=email, password=password)
            
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)
                
                token_data = {
                    "refresh": refresh_token,
                    "access": access_token,
                } 

                return Response(token_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "email or password incorrect"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    