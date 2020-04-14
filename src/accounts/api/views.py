from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    ListAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import (
    IsOwner,
)
from .serializers import (
    UserCreateSerializer,
    UserProfileSerializer,
    UserSerializer,
)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]


class MyAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        authentication_classes = [TokenAuthentication]
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user_id=user.id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email
        })


class UserProfileAPIView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    queryset = User.objects.all()
    lookup_field = 'pk'
    serializer_class = UserProfileSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
