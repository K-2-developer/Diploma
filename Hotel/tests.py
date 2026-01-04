from django.test import TestCase
from .models import Hotel

class HotelModelTest(TestCase):
    def test_create_hotel(self):
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
        hotel = Hotel.objects.create(
            hotel_name="Read Hotel",
            hotel_location="Minsk",
            hotel_rating=4
        )
        found = Hotel.objects.get(hotel_id=hotel.hotel_id)
        self.assertEqual(found.hotel_name, "Read Hotel")

    def test_update_hotel(self):
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
        hotel = Hotel.objects.create(
            hotel_name="Delete",
            hotel_location="Minsk",
            hotel_rating=2
        )
        hotel_id = hotel.hotel_id
        hotel.delete()
        self.assertFalse(Hotel.objects.filter(hotel_id=hotel_id).exists())
from django.test import TestCase

# Create your tests here.
