from booking.domain.interface.abstractRepositoryBooking import AbstractRepositoryBooking
from booking.domain.occupancy import Occupancy

class MemRepositoryBooking(AbstractRepositoryBooking):

    def __init__(self):
        self.items = []

    def findOccupancy(self, date, resource) -> Occupancy:
        result = filter(lambda book: book.resource.name == resource.name and book.date == date, self.items)
        return Occupancy(list(result))

    def save(self, booking):
        self.items.append(booking)