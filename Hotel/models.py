from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.TextField(max_length=100)
    hotel_location = models.TextField(max_length=100)
    hotel_description = models.TextField(max_length=500,null=True, blank=True)
    hotel_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.hotel_name


class HotelPhoto(models.Model):
    photo_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hotel_photos',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default='standart',blank=True)
    room_price = models.IntegerField()
    available = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Room {self.room_id} in {self.hotel_id.hotel_name}'


class RoomPhoto(models.Model):
    photo_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_photo = models.ImageField(upload_to='room_photos',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Booking:{self.booking_id}'