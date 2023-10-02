from rest_framework import viewsets
from session_app_tracker import models
from session_app_tracker.api import serializers

class UserViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    