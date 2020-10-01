from booking.domain.resource import Resource
from booking.domain.user import User
from booking.domain.booking import Booking

from datetime import date
import pytest

from mock.memRepositoryBooking import MemRepositoryBooking


def test_OneBookingSuccess():
    repositoryBooking = MemRepositoryBooking()
    resource = Resource("Vila Mariana", 5)
    user = User("joao.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user, resource, occupancy)
    assert booking.confirmation == True

def test_bookingFailedByUser():
    repositoryBooking = MemRepositoryBooking()
    resource = Resource("Vila Mariana", 5)
    user = User("joao.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user, resource, occupancy)
    repositoryBooking.save(booking)

    occupancy = repositoryBooking.findOccupancy(date.today(), resource)

    with pytest.raises(Exception):
        booking = Booking(date.today(), user, resource, occupancy)

def test_bookingFailedOverbooking():
    repositoryBooking = MemRepositoryBooking()
    resource = Resource("Vila Mariana", 3)

    user = User("joao.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user, resource, occupancy)
    repositoryBooking.save(booking)

    user2 = User("jose.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user2, resource, occupancy)
    repositoryBooking.save(booking)

    user3 = User("patricia.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user3, resource, occupancy)
    repositoryBooking.save(booking)

    occupancy = repositoryBooking.findOccupancy(date.today(), resource)

    user4 = User("mariana.silva")

    with pytest.raises(Exception):
        booking = Booking(date.today(), user4, resource, occupancy)


def test_bookingOneOrMoreBookingSucess():
    repositoryBooking = MemRepositoryBooking()
    resource = Resource("Vila Mariana", 3)

    user = User("joao.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user, resource, occupancy)
    repositoryBooking.save(booking)

    user2 = User("jose.silva")
    occupancy = repositoryBooking.findOccupancy(date.today(), resource)
    booking = Booking(date.today(), user2, resource, occupancy)
    repositoryBooking.save(booking)

    occupancy = repositoryBooking.findOccupancy(date.today(), resource)

    user3 = User("mariana.silva")

    booking = Booking(date.today(), user3, resource, occupancy)
    assert booking.confirmation == True
