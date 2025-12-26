from rest_framework import serializers
from .models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_name', 'hotel_location', 'hotel_description', 'hotel_rating')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_id', 'hotel_id', 'type', 'room_price', 'available')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id', 'user_id', 'room_id', 'check_in', 'check_out')


class HotelPopularitySerializer(serializers.Serializer):
    hotel_id = serializers.IntegerField()
    hotel_name = serializers.CharField()
    booking_quantity = serializers.IntegerField()


class AdminStatisticSerializer(serializers.Serializer):
    bookings = serializers.IntegerField()
    canceled_bookings = serializers.IntegerField()
    active_bookings = serializers.IntegerField()
    hotels = HotelPopularitySerializer(many=True)


