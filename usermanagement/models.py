from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        max_length=100
    )
    
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    
    
    
    
    
class UserProfiles(models.Model):
    user = models.OneToOneField('MyUser',primary_key=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=13,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    profile_picture = models.ImageField(upload_to='userprofiles/',null=True,blank=True)