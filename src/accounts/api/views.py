from django.contrib.auth import get_user_model

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .serializers import (
    UserCreateUpdateSerializer,
    UserDetailSerializer,
    UserLoginSerializer,
)

from .permissions import (
    IsOwner,
)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserDetailSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class UserUpdateAPIView(UpdateAPIView):
#     permission_classes = [IsOwner]
#     serializer_class = UserCreateUpdateSerializer
#     queryset = User.objects.all()

'''
curl -X POST -d "username=mahd&password=Super@RandomPass_38" http://localhost:8000/api/auth/token
'''
