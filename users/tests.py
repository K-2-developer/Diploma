from django.test import TestCase, Client
from django.contrib.auth.models import User
from Hotel.models import Hotel,Room,Booking
from users.models import Review

class IntegrationTest(TestCase):
    '''A class for testing integrations'''

    def setUp(self):
        '''Creating test objects for integration tests'''
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='t@gmail.com', password='12345')
        self.admin = User.objects.create_superuser(username='admin', email='t2@gmail.com', password='11111')
        self.hotel = Hotel.objects.create(hotel_name="Test Hotel", hotel_location="Belarus", hotel_rating=5)
        self.room = Room.objects.create(hotel_id=self.hotel, type="standard", room_price=100, available=True)

    def test_booking(self):
        '''Testing booking functionality'''
        self.client.login(username='test', password='12345')
        response = self.client.post(
            f"/room/{self.room.room_id}/booking/",
            {"check_in": "2026-01-10",
             "check_out": "2026-01-15"
             })
        self.assertEqual(response.status_code, 302)
        booking = Booking.objects.get(room_id=self.room, user_id=self.user)
        self.assertEqual(str(booking.check_in), "2026-01-10")
        self.assertEqual(str(booking.check_out), "2026-01-15")

    def test_cancel_booking(self):
        '''Testing canceling booking'''
        self.client.login(username='test', password='12345')
        booking = Booking.objects.create(
            room_id=self.room, user_id=self.user,
            check_in='2026-01-10',
            check_out='2026-01-15'
        )
        response = self.client.get(f"/cancel_booking/{booking.booking_id}/")
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertTrue(booking.deleted)
        self.assertIsNotNone(booking.deleted_at)

    def test_profile_booking(self):
        '''Testing bookings in profile'''
        self.client.login(username='test', password='12345')
        Booking.objects.create(
            room_id=self.room,
            user_id=self.user,
            check_in='2026-01-10', check_out='2026-01-15'
        )
        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Hotel")
