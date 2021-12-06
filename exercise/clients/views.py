from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from clients.models import User
from clients.serializers import ListUserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    pagination_class = LimitOffsetPagination
