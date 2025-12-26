from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from Hotel.forms import BookingForm
from Hotel.models import Hotel, Room, Booking
from Hotel.serializers import HotelSerializer, RoomSerializer, BookingSerializer, AdminStatisticSerializer, \
    HotelPopularitySerializer
from users.models import Review
from django.contrib import messages
from datetime import datetime
from users.forms import ReviewForm


def index(request):
    hotels = Hotel.objects.all()
    return render(request, 'index.html', {'hotels': hotels})


def hotel_info(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    rooms = Room.objects.filter(hotel_id=hotel)
    reviews = Review.objects.filter(hotel=hotel)
    return render(request, 'hotel_info.html', {
        'hotel': hotel,
        'rooms': rooms,
        'reviews': reviews,
        'form': ReviewForm()
    })


@login_required
def booking(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        form.room = room
        if form.is_valid():
            booking = form.save(commit=False)  # In order to fill up fields before saving
            booking.user_id = request.user
            booking.room_id = room
            booking.save()
            days = (booking.check_out - booking.check_in).days
            total_price = days * room.room_price
            messages.success(request, f'Total price: ${total_price}')
            return redirect('booking_succeed')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form, 'room': room})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user_id = request.user)
    booking.deleted = True
    booking.deleted_at = datetime.now()
    booking.save()
    return redirect('profile')

@login_required
def booking_succeed(request):
    return render(request, 'booking_succeed.html')


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


class AdminStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        bookings = Booking.objects.count()
        canceled_bookings = Booking.objects.filter(deleted=True).count()
        active_bookings = Booking.objects.filter(deleted=False).count()
        hotels = Hotel.objects.annotate(booking_quantity=Count('room__booking')).order_by('-booking_quantity')
        serialized_hotels = HotelPopularitySerializer(hotels, many=True).data
        data = {'bookings': bookings,
                'canceled_bookings': canceled_bookings,
                'active_bookings': active_bookings,
                'hotels': serialized_hotels,}
        serializer = AdminStatisticSerializer(data)
        return Response(serializer.data)


