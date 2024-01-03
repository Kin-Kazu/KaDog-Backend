# events/serializers.py

from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.Serializer):
    key = serializers.IntegerField()
    number = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    dog_name = serializers.CharField(max_length=100)
    dog_breed = serializers.CharField(max_length=100)
    size = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Event
        fields = '__all__'
