from django import forms
from django.core.exceptions import ValidationError
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out',]

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        room = self.room
        if check_in and check_out:  # Checking for not None
            if check_in > check_out:
                raise ValidationError('Something went wrong.')
            elif check_in == check_out:
                raise ValidationError('U cant book a room for less than 2 days.')
        bookings = Booking.objects.filter(room_id=room, check_in__lt=check_out, check_out__gt=check_in, deleted=False)
        if bookings.exists():
            raise ValidationError('For these days room is already booked. Please choose another room or date.')
        return cleaned_data