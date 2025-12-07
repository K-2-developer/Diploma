from django import http
from django.shortcuts import render
# from Hotel.forms import CreateHotel
from Hotel.models import Hotel, Room


def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})

def hotel_info(request, hotel_id):
    hotel = Hotel.objects.get(hotel_id=hotel_id)
    rooms = Room.objects.filter(hotel_id=hotel)
    return render(request, 'hotel_info.html', {'hotel': hotel, 'rooms': rooms})


