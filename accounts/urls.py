from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

urlpatterns = [ 
    path("", views.UserCreateDeleteView.as_view()), 
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", views.LogoutAPIView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("validate/username/", views.ValidUsernameView.as_view()),
    path("validate/email/", views.ValidEmailView.as_view()),
    path("password/", views.ChangePasswordView.as_view()),
    path("<str:name>/", views.ProfileView.as_view()),
    
]