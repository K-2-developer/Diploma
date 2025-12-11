from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Hotel, Review


def review(request,hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel
            review.save()
            return redirect('hotel_info', pk=hotel.id) #redirect?
    else:
        form = ReviewForm()
        return render(request, 'hotel_info.html', {'form': form,
                                                   'hotel': hotel,
                                                   'reviews': hotel.review.all()})

