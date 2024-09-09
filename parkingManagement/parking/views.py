from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ParkingSpot, Ticket
from .serializers import ParkingSpotSerializer, TicketSerializer
import logging

# Create your views here.

# Get all parking spots and their statuses
class ParkingSpotListView(APIView):
    def get(self, request):
        spots = ParkingSpot.objects.all()
        serializer = ParkingSpotSerializer(spots, many=True)
        return Response(serializer.data)

# Get a ticket for a parking spot (create ticket and occupy spot)
class TicketCreateView(APIView):
    def post(self, request, spot_number):
        try:
            spot = ParkingSpot.objects.get(spot_number=spot_number, is_occupied=False)
            ticket = Ticket.objects.create(spot=spot)
            spot.is_occupied = True
            spot.save()
            return Response(TicketSerializer(ticket).data, status=status.HTTP_201_CREATED)
        except ParkingSpot.DoesNotExist:
            return Response({"error": "Parking spot is unavailable or does not exist."}, status=status.HTTP_400_BAD_REQUEST)

# Release a parking spot (deactivate ticket and free spot)
class TicketReleaseView(APIView):
    def post(self, request, spot_number):
        try:
            spot = ParkingSpot.objects.get(spot_number=spot_number, is_occupied=True)
            ticket = Ticket.objects.get(spot_id=spot.id, is_active=True)
            ticket.is_active = False
            ticket.save()
            spot.is_occupied = False
            spot.save()
            return Response({"message": "Parking spot is now free."}, status=status.HTTP_200_OK)
        except ParkingSpot.DoesNotExist:
            return Response({"error": "Parking spot is already free or does not exist."}, status=status.HTTP_400_BAD_REQUEST)
