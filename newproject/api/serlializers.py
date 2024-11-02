from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class ItemSerlializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = ('id' ,'category', 'subcategory', 'name', 'amount')

class UserSerlializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']