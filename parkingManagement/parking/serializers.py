# serializers.py in parking app
from rest_framework import serializers
from .models import ParkingSpot, Ticket

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['spot_number', 'is_occupied']

class TicketSerializer(serializers.ModelSerializer):
    spot = ParkingSpotSerializer()

    class Meta:
        model = Ticket
        fields = ['spot', 'issued_at', 'is_active', 'id']
