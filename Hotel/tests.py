from django.test import TestCase
from .models import Hotel, HotelPhoto


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
            hotel_name = 'Test Hotel',
            hotel_location = 'Test Location',
            hotel_description = 'Test Description',
            hotel_rating = 5
        )

    def test_hotel_photo(self):
        '''Test for Creating photo of hotel'''
        test_photo = HotelPhoto.objects.create(hotel_id=self.hotel)
        self.assertEqual(HotelPhoto.objects.count(), 1)
        self.assertEqual(test_photo.hotel_id.hotel_name, "Test Hotel")


    def test_read_hotel_photo(self):
        '''Test for Reading information about hotel photo'''
        photo = HotelPhoto.objects.create(hotel_id=self.hotel)
        found = HotelPhoto.objects.get(photo_id=photo.photo_id)
        self.assertEqual(found.hotel_id.hotel_name, "Test Hotel")


    def test_update_hotel_photo(self):
        '''Test for Updating hotel photo'''
        photo = HotelPhoto.objects.create(hotel_id=self.hotel)
        self.hotel.hotel_description = "Updated Description"
        self.hotel.save()
        updated = Hotel.objects.get(hotel_id=self.hotel.hotel_id)
        self.assertEqual(updated.hotel_description, "Updated Description")


    def test_delete_hotel_photo(self):
        '''Test for Deleting hotel photo'''
        photo = HotelPhoto.objects.create(hotel_id=self.hotel)
        photo_id = photo.photo_id
        photo.delete()
        self.assertFalse(HotelPhoto.objects.filter(photo_id=photo_id).exists())


