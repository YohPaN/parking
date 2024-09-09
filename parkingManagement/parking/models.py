from django.db import models
from django.utils import timezone

# Create your models here.

# models.py in parking app
class ParkingSpot(models.Model):
    spot_number = models.PositiveIntegerField(unique=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Spot {self.spot_number} - {'Occupied' if self.is_occupied else 'Free'}"

class Ticket(models.Model):
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE, related_name='ticket')
    issued_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Ticket for Spot {self.spot.spot_number} - {'Active' if self.is_active else 'Inactive'}"
