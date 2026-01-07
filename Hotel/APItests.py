from django.test import TestCase
from django.contrib.auth.models import User
from Hotel.models import Hotel, Room, Booking

class HotelAPITest(TestCase):
    '''A class for testing Hotel API'''

    def setUp(self):
        '''Setting up test hotels'''
        self.hotel1 = Hotel.objects.create(
            hotel_name='Test1',
            hotel_location="Minsk",
            hotel_description="Test1",
            hotel_rating=4
        )
        self.hotel2 = Hotel.objects.create(
            hotel_name="Test2",
            hotel_location="Minsk",
            hotel_description="Test2",
            hotel_rating=5
        )

    def test_hotel_list(self):
        '''Testing API view for hotel list'''
        response = self.client.get("/api/v1/hotels/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        hotel_names = [hotel["hotel_name"] for hotel in data]
        self.assertIn("Test1", hotel_names)
        self.assertIn("Test2", hotel_names)
        self.assertEqual(len(data), 2)

    def test_hotel_info(self):
        '''Testing hotel info API view'''
        response = self.client.get(f"/api/v1/hotels/{self.hotel1.hotel_id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["hotel_name"], "Test1")


class RoomAPITest(TestCase):
    '''A class for testing Room API'''

    def setUp(self):
        '''Setting up test rooms'''
        self.hotel = Hotel.objects.create(
            hotel_name="Test1",
            hotel_location="Minsk",
            hotel_rating=5
        )
        self.room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=100,
            available=True
        )
        self.room2 = Room.objects.create(
            hotel_id=self.hotel,
            type="VIP",
            room_price=500,
            available=False
        )

    def test_room_list(self):
        '''Testing API view for rooms'''
        response = self.client.get("/api/v1/rooms/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        room_types = [room["type"] for room in data]
        self.assertIn("standard", room_types)
        self.assertIn("VIP", room_types)
        self.assertEqual(len(data), 2)

    def test_room_info(self):
        '''Testing API view for room information'''
        response = self.client.get(f"/api/v1/rooms/{self.room.room_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["room_id"], self.room.room_id)
        self.assertEqual(data["type"], "standard")
        self.assertEqual(data["room_price"], 100)
        self.assertTrue(data["available"])

class BookingAPITest(TestCase):
    '''A class for testing Booking API'''


    def setUp(self):
        '''Setting up test objects'''
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.hotel = Hotel.objects.create(
            hotel_name="Test Hotel",
            hotel_location="Minsk",
            hotel_rating=5
        )
        self.room1 = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=100,
            available=True
        )
        self.room2 = Room.objects.create(
            hotel_id=self.hotel,
            type="luxury",
            room_price=200,
            available=True
        )
        self.booking1 = Booking.objects.create(
            user_id=self.user,
            room_id=self.room1,
            check_in="2026-01-10",
            check_out="2026-01-15"
        )
        self.booking2 = Booking.objects.create(
            user_id=self.user,
            room_id=self.room2,
            check_in="2026-02-01",
            check_out="2026-02-05"
        )

    def test_booking_list(self):
        '''Testing API view for booking list'''
        response = self.client.get("/api/v1/bookings/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        booking_ids = [b["booking_id"] for b in data]
        self.assertIn(self.booking1.booking_id, booking_ids)
        self.assertIn(self.booking2.booking_id, booking_ids)
        self.assertEqual(len(data), 2)

    def test_booking_info(self):
        '''Testing API view for booking info'''
        response = self.client.get(f"/api/v1/bookings/{self.booking1.booking_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["user_id"], self.user.id)
        self.assertEqual(data["room_id"], self.room1.room_id)


class UserAPITest(TestCase):
    '''A class for testing User API'''

    def setUp(self):
        '''Creating test user'''
        self.user = User.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="12345"
        )

    def test_user_info(self):
        '''Testing API view for user info'''
        response = self.client.get(f"/api/v1/user/{self.user.id}/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["username"], "testuser")
        self.assertEqual(data["email"], "test@gmail.com")

class AdminStatisticAPITest(TestCase):
    '''A class for testing admin statistic API'''

    def setUp(self):
        '''Setting up test objects'''
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass"
        )
        self.client.login(username="admin", password="adminpass")

        self.hotel = Hotel.objects.create(
            hotel_name="Test Hotel",
            hotel_location="Minsk",
            hotel_rating=5
        )
        self.room = Room.objects.create(
            hotel_id=self.hotel,
            type="standard",
            room_price=100,
            available=True
        )
        self.room2 = Room.objects.create(
            hotel_id=self.hotel,type="luxury",
            room_price=200,
            available=True
        )

        self.booking = Booking.objects.create(
            user_id=self.admin,
            room_id=self.room,
            check_in="2026-01-10",
            check_out="2026-01-15",
            deleted=False
        )
        self.booking2 = Booking.objects.create(
            user_id=self.admin,
            room_id=self.room2,
            check_in="2026-02-01",
            check_out="2026-02-05",
            deleted=True
        )

    def test_admin_stat(self):
        """Testing API view for admin statistic"""
        response = self.client.get("/api/v1/adminstatistic/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("bookings", data)
        self.assertIn("active_bookings", data)
        self.assertIn("canceled_bookings", data)
        self.assertIn("hotels", data)
        self.assertEqual(data["bookings"], 2)
        self.assertEqual(data["active_bookings"], 1)
        self.assertEqual(data["canceled_bookings"], 1)
        self.assertEqual(len(data["hotels"]), 1)
        self.assertEqual(data["hotels"][0]["hotel_name"], "Test Hotel")





