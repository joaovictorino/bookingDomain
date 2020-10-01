import abc
from booking.domain.occupancy import Occupancy

class AbstractRepositoryBooking(abc.ABC):

    @abc.abstractmethod
    def findOccupancy(self, date, resource) -> Occupancy:
        pass

    @abc.abstractmethod
    def save(self, booking):
        pass