
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView
from .forms import ReviewForm, RegistrationForm, ProfileUpdateForm
from .models import Hotel
from Hotel.models import Booking
from django.contrib.auth import logout
from .serializers import UserSerializer



@login_required
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
    booking = Booking.objects.filter(user_id=user, deleted = False)
    return render(request, 'profile.html', {'user': user, 'booking': booking})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'profile_update.html', {'form': form})



class UserAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

