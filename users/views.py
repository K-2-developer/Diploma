from urllib import request

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm, RegistrationForm
from .models import Hotel
from Hotel.models import Booking
from django.contrib.auth import logout


def review(request,hotel_id):
    hotel = get_object_or_404(Hotel, hotel_id=hotel_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel
            review.save()
            return redirect('hotel_info', hotel_id=hotel.hotel_id)
    else:
        form = ReviewForm()
        return render(request, 'hotel_info.html', {
            'form': form,
            'hotel': hotel,
            'reviews': hotel.reviews.all()
        })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    booking = Booking.objects.filter(user_id=user)
    return render(request, 'profile.html', {'user': user, 'booking': booking})

def user_logout(request):
    logout(request)
    return redirect('index')