from django import http
from django.shortcuts import render
from Hotel.forms import CreateHotel
from Hotel.models import Hotel


def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})





