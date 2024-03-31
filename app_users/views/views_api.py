from time import sleep

from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from app_users.models import User
from app_users.permissions import IsPhone, IsVerifyPhone
from app_users.serializers.serializers_api import ProfileUserSerializer, RegisterUserSerializer, PhoneSerializer, \
    CodeSerializer
from app_users.utils import create_code, create_invite_code


class RegisterUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class ProfileAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileUserSerializer
    permission_classes = [IsAuthenticated, IsPhone, IsVerifyPhone]


class PhoneAPIView(APIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PhoneSerializer

    def post(self, request, *args, **kwargs):
        user_phone = request.data['phone']
        try:
            get_object_or_404(User, phone=user_phone)
        except Http404:
            return response.Response('Номер телефона не зарегестрирован')
        else:
            user = self.queryset.get(phone=user_phone)
            user.code = create_code()
            user.save()
            sleep(2)
        return response.Response({'code': user.code})


class VerifyPhoneAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = CodeSerializer

    def patch(self, request, pk):
        user = self.queryset.get(pk=pk)
        user_code = request.data['code']

        if user_code == user.code:
            user.phone_verify = True
            user.invite_code = create_invite_code()
            user.save()
            return response.Response('Верификация номера телефона прошла успешно')
        else:
            return response.Response('Код введен не верно, попробуйте еще раз')
