from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    groups = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:

        model = User
        read_only_fields = [field.name for field in User._meta.fields]
        depth = 1
        exclude = ['password', 'is_superuser', 'is_staff', 'last_login', 'date_joined', 'user_permissions']