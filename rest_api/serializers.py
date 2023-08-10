from rest_framework import serializers
from hub.models import HubDoggyModel


class HubSerializer(serializers.ModelSerializer):

    class Meta:
        model = HubDoggyModel
        fields = '__all__'
