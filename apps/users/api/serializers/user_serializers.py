from rest_framework import serializers
from apps.users.models import User

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('state', 'create_date', 'modified_date',)