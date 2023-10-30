from rest_framework import serializers
from .models import MyUser,UserProfiles
from rest_framework.exceptions import ValidationError


class UserRegistrationSerilaizer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'passowrd'},write_only=True)
    class Meta:
        model = MyUser
        fields = ('username','email','password','password2')
        
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError('Password does not match')
        return attrs   
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  
    password = serializers.CharField()  
    
class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username','email')    


        
class UserProfileViewSerializer(serializers.ModelSerializer):
    user = UserViewSerializer()
    class Meta:
        model = UserProfiles
        fields = ('user','first_name','phone','last_name','date_of_birth','profile_picture')