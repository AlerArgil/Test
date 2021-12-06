from rest_framework import generics

from clients.models import User
from clients.serializers import ListUserSerializer


class UserList(generics.ListAPIView):
    """
    User List view
    """
    queryset = User.objects.prefetch_related('add_infos').all()
    serializer_class = ListUserSerializer
