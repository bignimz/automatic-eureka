from rest_framework import viewsets
from . import models
from . import serializers


class ChildViewset(viewsets.ModelViewSet):
    queryset = models.Child.objects.all()
    serializer_class = serializers.ChildSerializer
