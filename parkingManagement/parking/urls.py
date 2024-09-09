from django.urls import path
from .views import ParkingSpotListView, TicketCreateView, TicketReleaseView

urlpatterns = [
    path('spots/', ParkingSpotListView.as_view(), name='spot-list'),
    path('ticket/create/<int:spot_number>/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/release/<int:spot_number>/', TicketReleaseView.as_view(), name='ticket-release'),
]
