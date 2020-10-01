from booking.domain.occupancy import Occupancy

class Booking:
    def __init__(self, date, user, resource, occupancy: Occupancy):

        if occupancy.userHasAlreadyBooked(user):
            raise Exception("User has already booked for this day")

        if resource.isFull(occupancy):
            raise Exception("Resource is full")

        self.date = date
        self.user = user
        self.resource = resource
        self.confirmation = True