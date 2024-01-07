from rest_framework import serializers
from .models import menu, booking

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'


class BookingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'