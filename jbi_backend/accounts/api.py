from rest_framework import viewsets, permissions, generics, status

from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth.models import User
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    LoginSerializer,
    UserDetailsSerializer,
)
import re
from accounts.models import User, UserDetails, JBIDetails


# register api
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


# login api
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {  # tambah disini buat bikin addition response
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


# get current user api
class UserApi(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    # TODO diganti returnnya supaya lebih detailed
    def get_object(self):
        return self.request.user


# api untuk update user details (BUKAN JBI details)
class SelfDetailsAPI(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        details = UserDetails.objects.get(user=self.request.user)
        user = self.request.user
        if details.role == "JBI":
            jbi_details = JBIDetails.objects.get(jbi_username=user.username)
            return Response(
                {
                    "user_id": user.id,
                    "name": user.username,
                    "lembaga": jbi_details.nama_lembaga,
                    "phone": details.phone,
                    "email": user.email,
                    "gender": details.gender,
                    "is_available": not jbi_details.is_nonactive,
                    "diluar_jadwal": jbi_details.diluar_jadwal,
                }
            )

        return Response(
            {
                "user_id": user.id,
                "name": user.username,
                "phone": details.phone,
                "email": user.email,
                "gender": details.gender,
                "is_activated": details.is_activated,
            }
        )
