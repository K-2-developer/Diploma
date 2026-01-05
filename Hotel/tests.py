from django.test import TestCase
from .models import Hotel, HotelPhoto, Room, RoomPhoto, Booking


class HotelModelTest(TestCase):
    '''A class to test CRUD operations for Hotel model'''

    def test_create_hotel(self):
        '''Test for creating a hotel'''
        hotel = Hotel.objects.create(
            hotel_name="Grand Hotel",
            hotel_location="Minsk",
            hotel_description="Test",
            hotel_rating=5
        )
        self.assertEqual(Hotel.objects.count(), 1)
        self.assertEqual(hotel.hotel_name, "Grand Hotel")
        self.assertEqual(hotel.hotel_location, "Minsk")
        self.assertEqual(hotel.hotel_rating, 5)

    def test_read_hotel(self):
        '''Test for reading hotel information'''
        hotel = Hotel.objects.create(
            hotel_name="Read Hotel",
            hotel_location="Minsk",
            hotel_rating=4
        )
        found = Hotel.objects.get(hotel_id=hotel.hotel_id)
        self.assertEqual(found.hotel_name, "Read Hotel")

    def test_update_hotel(self):
        '''Test for updating hotel information'''
        hotel = Hotel.objects.create(
            hotel_name="Update",
            hotel_location="Minsk",
            hotel_rating=3
        )
        hotel.hotel_name = "New Name"
        hotel.hotel_rating = 4
        hotel.save()
        updated = Hotel.objects.get(hotel_id=hotel.hotel_id)
        self.assertEqual(updated.hotel_name, "New Name")
        self.assertEqual(updated.hotel_rating, 4)

    def test_delete_hotel(self):
        '''Test for deleting hotel'''
        hotel = Hotel.objects.create(
            hotel_name="Delete",
            hotel_location="Minsk",
            hotel_rating=2
        )
        hotel_id = hotel.hotel_id
        hotel.delete()
        self.assertFalse(Hotel.objects.filter(hotel_id=hotel_id).exists())


class HotelPhotoModelTest(TestCase):
    '''A class to test CRUD operations with hotel photos'''

    def setUp(self):
        '''A func to create an abstract hotel for testing CRUD photo operations'''
        self.hotel = Hotel.objects.create(
            hotel_name='Test Hotel',
            hotel_location='Test Location',
            hotel_description='Test Description',
            hotel_rating=5
        )

    def test_hotel_photo(self):
        '''Test for Creating photo of hotel'''
        photo = HotelPhoto.objects.create(
            hotel_id=self.hotel,
            photo="old_photo.jpg"
        )
        self.assertEqual(HotelPhoto.objects.count(), 1)
        self.assertEqual(photo.photo, "old_photo.jpg")

    def test_read_hotel_photo(self):
        '''Test for Reading information about hotel photo'''
        photo = HotelPhoto.objects.create(
            hotel_id=self.hotel,
            photo="read_photo.jpg"
        )
        found = HotelPhoto.objects.get(photo_id=photo.photo_id)
        self.assertEqual(found.photo, "read_photo.jpg")

    def test_update_hotel_photo(self):
        '''Test for Updating hotel photo'''
        photo = HotelPhoto.objects.create(
            hotel_id=self.hotel,
            photo="old_photo.jpg"
        )
        photo.photo = "new_photo.jpg"
        photo.save()
        updated = HotelPhoto.objects.get(photo_id=photo.photo_id)
        self.assertEqual(updated.photo, "new_photo.jpg")

    def test_delete_hotel_photo(self):
        '''Test for Deleting hotel photo'''
        photo = HotelPhoto.objects.create(
            hotel_id=self.hotel,
            photo="delete_photo.jpg"
        )
        photo_id = photo.photo_id
        photo.delete()
        self.assertFalse(HotelPhoto.objects.filter(photo_id=photo_id).exists())


class RoomModelTest(TestCase):
    '''A class to test CRUD operations with rooms'''

    def setUp(self):
        '''A func to create an abstract hotel for testing CRUD operations'''
        self.hotel = Hotel.objects.create(
            hotel_name="Test Hotel",
            hotel_location="Minsk",
            hotel_description="Test Description",
            hotel_rating=5
        )

    def test_create_room(self):
        '''Test for creating a room'''
        room = Room.objects.create(
            hotel_id=self.hotel,
            type="deluxe",
            room_price=100,
            available=True
        )
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(room.type, "deluxe")
        self.assertTrue(room.available)

    def test_read_room(self):
        '''Test for reading room information'''
        room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=50,
            available=False
        )
        found = Room.objects.get(room_id=room.room_id)
        self.assertEqual(found.type, "standard")
        self.assertEqual(found.room_price, 50)
        self.assertFalse(found.available)

    def test_update_room(self):
        '''Test for updating room information'''
        room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=50,
            available=True
        )
        room.room_price = 80
        room.available = False
        room.save()
        updated = Room.objects.get(room_id=room.room_id)
        self.assertEqual(updated.room_price, 80)
        self.assertFalse(updated.available)

    def test_delete_room(self):
        '''Test for deleting room'''
        room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=50,
            available=True
        )
        room_id = room.room_id
        room.delete()
        self.assertFalse(Room.objects.filter(room_id=room_id).exists())


class RoomPhotoModelTest(TestCase):
    '''A class to test CRUD operations with room photos'''

    def setUp(self):
        '''Create a hotel and room for testing CRUD operations with room photo'''
        self.hotel = Hotel.objects.create(
            hotel_name="Test Hotel",
            hotel_location="Minsk",
            hotel_description="Test Description",
            hotel_rating=5
        )
        self.room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=50,
            available=True
        )

    def test_create_room_photo(self):
        '''Test for Creating a room photo'''
        photo = RoomPhoto.objects.create(
            room_id=self.room,
            room_photo="room_old.jpg"
        )
        self.assertEqual(RoomPhoto.objects.count(), 1)
        self.assertEqual(photo.room_photo.name, "room_old.jpg")

    def test_read_room_photo(self):
        '''Test for Reading a room photo'''
        photo = RoomPhoto.objects.create(
            room_id=self.room,
            room_photo="room_read.jpg"
        )
        found = RoomPhoto.objects.get(photo_id=photo.photo_id)
        self.assertEqual(found.room_photo.name, "room_read.jpg")

    def test_update_room_photo(self):
        '''Test for Updating a room photo'''
        photo = RoomPhoto.objects.create(
            room_id=self.room,
            room_photo="room_old.jpg"
        )
        photo.room_photo = "room_new.jpg"
        photo.save()
        updated = RoomPhoto.objects.get(photo_id=photo.photo_id)
        self.assertEqual(updated.room_photo.name, "room_new.jpg")

    def test_delete_room_photo(self):
        '''Test for Deleting a room photo'''
        photo = RoomPhoto.objects.create(
            room_id=self.room,
            room_photo="room_delete.jpg"
        )
        photo_id = photo.photo_id
        photo.delete()
        self.assertFalse(RoomPhoto.objects.filter(photo_id=photo_id).exists())


class BookingModelTest(TestCase):
    '''A class to test CRUD operations with bookings'''

    def setUp(self):
        '''Create a hotel and room for testing CRUD operations with room photo'''
        self.hotel = Hotel.objects.create(
            hotel_name="Test Hotel",
            hotel_location="Minsk",
            hotel_description="Test Description",
            hotel_rating=5
        )
        self.room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=50,
            available=True
        )

    def test_create_booking(self):
        '''Test for creating a booking'''
        booking = Booking.objects.create(
            room=self.room,
            customer_name="John Doe",
            check_in="2026-01-10",
            check_out="2026-01-15"
        )
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(booking.room, self.room)
        self.assertEqual(booking.customer_name, "John Doe")

    def test_read_booking(self):
        '''Test for reading a booking'''
        booking = Booking.objects.create(
            room=self.room,
            customer_name="Jane Doe",
            check_in="2026-02-01",
            check_out="2026-02-05"
        )
        found = Booking.objects.get(pk=booking.pk)
        self.assertEqual(found.customer_name, "Jane Doe")
        self.assertEqual(found.room, self.room)

    def test_update_booking(self):
        '''Test for updating a booking'''
        booking = Booking.objects.create(
            room=self.room,
            customer_name="Alex",
            check_in="2026-03-01",
            check_out="2026-03-10"
        )
        booking.customer_name = "Alex Updated"
        booking.save()
        updated = Booking.objects.get(pk=booking.pk)
        self.assertEqual(updated.customer_name, "Alex Updated")

    def test_delete_booking(self):
        '''Test for deleting a booking'''
        booking = Booking.objects.create(
            room=self.room,
            customer_name="Delete Me",
            check_in="2026-04-01",
            check_out="2026-04-05"
        )
        booking_id = booking.pk
        booking.delete()
        self.assertFalse(Booking.objects.filter(pk=booking_id).exists())

