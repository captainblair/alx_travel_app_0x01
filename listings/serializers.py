# listings/serializers.py
from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'listing_id',
            'title',
            'description',
            'location',
            'price_per_night',
            'host',
            'created_at',
        ]
        read_only_fields = ('listing_id', 'created_at')


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.UUIDField(write_only=True, required=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'listing',
            'listing_id',
            'user',
            'start_date',
            'end_date',
            'status',
            'created_at',
        ]
        read_only_fields = ('booking_id', 'created_at')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
