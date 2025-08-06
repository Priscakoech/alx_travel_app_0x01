from django.shortcuts import render

# Create your views here.
#create viewsets for Listing and Booking using Django REST framework’s ModelViewSet.
#Ensure that these views provide CRUD operations for both models.from django.shortcuts import render
from .models import Listing, Booking
from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer.

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    