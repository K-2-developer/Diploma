from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm, RegistrationForm
from .models import Hotel, Review


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
    return render(request, 'register.html', {'form': form})