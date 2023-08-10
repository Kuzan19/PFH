from django.shortcuts import render
from rest_framework import generics
from hub.models import HubDoggyModel
from .serializers import HubSerializer


class HubAPIView(generics.ListAPIView):
    queryset = HubDoggyModel.objects.all()
    serializer_class = HubSerializer
