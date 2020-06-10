from backoffice.models import User
from api.serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class UserListCreateView(generics.ListCreateAPIView):
    """
        GET, CREATE
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'username')

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
