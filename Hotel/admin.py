from django.contrib import admin
from Hotel.models import Hotel, HotelPhoto
from Hotel.models import Room, RoomPhoto


admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelPhoto)
admin.site.register(RoomPhoto)

# Register your models here.
