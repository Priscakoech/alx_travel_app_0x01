#serializers for listings and booking models
from rest_framework import serializers
from .models import Listing, Booking
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'  # Include all fields from the Listing model

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Include all fields from the Booking model
        