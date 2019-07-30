from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Register
from .serializers import RegisterSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
