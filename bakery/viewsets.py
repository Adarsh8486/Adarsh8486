from rest_framework import  viewsets
from . import models
from . import serializer


class IngredientsViewset(viewsets.ModelViewSet):
    queryset = models.Ingredients.objects.all()
    serializer_class = serializer.IngredientsSerializers


class registerUserViewset(viewsets.ModelViewSet):
    queryset = models.registerUser.objects.all()
    serializer_class = serializer.registerUserSerializers
