from rest_framework import serializers
from .models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('hotel_id', 'hotel_name', 'hotel_location', 'hotel_description', 'hotel_rating')