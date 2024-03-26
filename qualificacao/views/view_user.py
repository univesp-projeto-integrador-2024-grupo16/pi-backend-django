from rest_framework import viewsets
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response

from django.contrib.auth.models import User

from ..serializers.user_serializer import UserSerializer

class UserView(viewsets.ReadOnlyModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

