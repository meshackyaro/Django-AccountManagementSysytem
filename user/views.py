from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer
from .models import User


# Create your views here.

# class UserRegister(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
