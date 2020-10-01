class Occupancy:
    def __init__(self, listOfBookings):
        self.listOfBookings = listOfBookings

    def userHasAlreadyBooked(self, user):
        result = [book for book, item in enumerate(self.listOfBookings) if item.user.login == user.login]

        if len(result) > 0:
            return True
        else:
            return False

    def getTotal(self):
        return len(self.listOfBookings)
