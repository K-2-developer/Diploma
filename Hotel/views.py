from django import http
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView

from Hotel.forms import BookingForm
from Hotel.models import Hotel, Room, Booking
from Hotel.serializers import HotelSerializer, RoomSerializer, BookingSerializer


def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})


def hotel_info(request, hotel_id):
    hotel = Hotel.objects.get(hotel_id=hotel_id)
    rooms = Room.objects.filter(hotel_id=hotel)
    return render(request, 'hotel_info.html', {'hotel': hotel, 'rooms': rooms})


def booking(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)  # In order to fill up fields before saving
            booking.user_id = request.user
            booking.room_id = room
            booking.save()
            return render(request, 'booking_succeed.html')  # Подумать над добавлением redirect вместо render!
    return render(request, 'booking.html', {'form': form, 'room': room})


class HotelAPIView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelInfoAPIView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class RoomAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomInfoAPIView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingAPIView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingInfoAPIView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer