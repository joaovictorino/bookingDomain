from booking.domain.occupancy import Occupancy

class Resource:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def isFull(self, occupancy: Occupancy):
        return occupancy.getTotal() == self.capacity