from django import forms
from .models import Hotel, HotelPhoto, Room, RoomPhoto


class CreateHotel(forms.Form):
    class Meta:
        model = Hotel
        fields = ('hotel_name','hotel_location')


