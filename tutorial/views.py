from django.contrib.auth.models import (
    User,
    Group
)
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import (
    UserSerializer,
    GroupSerializer
)
from django.shortcuts import render



# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be related
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_class =  [permissions.IsAuthenticated]
