from django.db import models


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.TextField(max_length=100)
    hotel_location = models.TextField(max_length=100)
    hotel_photos = models.ImageField(upload_to='hotel_photos')
    hotel_rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.hotel_name


class HotelPhoto(models.Model):
    photo_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hotel_photos')
    created_at = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_photos = models.ImageField(upload_to='room_photos')
    room_price = models.IntegerField()
    available = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField()

    def __str__(self):
        return self.room_id


class RoomPhoto(models.Model):
    photo_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_photo = models.ImageField(upload_to='room_photos')
    created_at = models.DateTimeField(auto_now_add=True)
