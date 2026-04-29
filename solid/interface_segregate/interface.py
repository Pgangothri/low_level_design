from abc import ABC, abstractmethod


class RiderInterface(ABC):
    @abstractmethod
    def book_ride(self):
        pass

    @abstractmethod
    def rate_driver(self):
        pass


class DriverInterface(ABC):
    @abstractmethod
    def accept_ride(self):
        pass

    @abstractmethod
    def track_earnings(self):
        pass

    @abstractmethod
    def rate_passenger(self):
        pass


class Rider(RiderInterface):
    def bookRide(self):  # yes
        pass

    def rateDriver(self):  # yes
        pass


class Driver(DriverInterface):
    def acceptRide(self):  # yes
        pass

    def trackEarnings(self):  # yes
        pass

    def ratePassenger(self):  # yes
        pass
