from booking.domain.resource import Resource
from booking.domain.user import User
from booking.domain.booking import Booking

from datetime import date

def test_bookingSuccess():
    resource = Resource("Vila Mariana", 5)
    user = User("joao.silva")
    booking = Booking(date.today(), user, resource)
    assert booking.confirmation == true

def test_bookingFailedByUser():
    pass

def test_bookingFailedOverbooking():
    pass
