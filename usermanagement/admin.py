from django.contrib import admin
from .models import MyUser,UserProfiles
# Register your models here.

admin.site.register(MyUser)
admin.site.register(UserProfiles)