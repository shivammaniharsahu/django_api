from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Register
        fields = ('id', 'name', 'email', 'contact', 'password', 'confirm_password')
