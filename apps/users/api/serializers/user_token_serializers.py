from django.contrib.auth import models
from rest_framework import serializers
from apps.users.models import User

class UserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name',)