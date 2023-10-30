from django.shortcuts import render
from .models import MyUser,UserProfiles
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    UserRegistrationSerilaizer,
    UserProfileViewSerializer,
    LoginSerializer
    )
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.



class UserRegistration(APIView):
    def post(self,request):
        print(request.data)
        seriailzer = UserRegistrationSerilaizer(data=request.data)
        if seriailzer.is_valid():
            passwrod=seriailzer.validated_data.get('password')
            user = User.objects.create_user(
                username=seriailzer.validated_data.get('username'),
                email=seriailzer.validated_data.get('email'),
                password=make_password(passwrod)
            )   
            UserProfiles.objects.create(user=user) 
            return Response({'msg':"user Registration Succesfull"},status=status.HTTP_200_OK)
        return Response(seriailzer.errors,status=status.HTTP_400_BAD_REQUEST)
        

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@permission_classes([IsAuthenticated])
class UserProfielView(APIView):
    def get(self,request):
        user = UserProfiles.objects.get(user=request.user)
        serializer = UserProfileViewSerializer(user)
        return Response(serializer.data)