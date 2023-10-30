from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('',views.UserRegistration.as_view(),name='registeration'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('userprofile/',views.UserProfielView.as_view(),name='userprofile')
]