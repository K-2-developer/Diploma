from django.contrib import admin
from Hotel.models import Hotel, HotelPhoto, Booking
from Hotel.models import Room, RoomPhoto


admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelPhoto)
admin.site.register(RoomPhoto)
admin.site.register(Booking)

# Register your models here.
