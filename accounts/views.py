from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from .serializer import UserSerializer, UserProfileSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


class UserCreateDeleteView(APIView):
    def post(self, request):
        data = request.data.copy() 
        data['password'] = make_password(data.get('password'))
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        user = request.user
        password = request.data.get('password')
        if not check_password(password, user.password):
            return Response({"error": "Invalid password."},status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_200_OK)
    
class ValidUsernameView(APIView):
    def get(self, request):
        username = request.query_params.get('username')
        if not username:
            return Response({'valid': False, 'message': 'Input username'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'valid': False, 'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'valid': True, 'message': 'Username is available'}, status=status.HTTP_200_OK)

class ValidEmailView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'valid': False, 'message': 'Input email'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'valid': False, 'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'valid': True, 'message': 'Email is available'}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"message": "Logout Success"}, status=status.HTTP_200_OK)
            except:
                return Response({"error": "This Token is invalid."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Input refresh value"}, status=status.HTTP_400_BAD_REQUEST)
        
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        username = self.kwargs['name']
        return User.objects.filter(username=username)

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        user = request.user
        print(user)
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if not user.check_password(old_password):
            return Response({'error': 'Old password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)