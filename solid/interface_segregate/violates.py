from abc import ABC, abstractmethod


# Abstract Base Class in Python
class UberUser(ABC):
    @abstractmethod
    def bookRide(self):
        pass

    @abstractmethod
    def acceptRide(self):
        pass

    @abstractmethod
    def trackEarnings(self):
        pass

    @abstractmethod
    def ratePassenger(self):
        pass

    @abstractmethod
    def rateDriver(self):
        pass


class Rider(UberUser):
    def bookRide(self):  # yes
        pass

    def acceptRide(self):  # not needed
        pass

    def trackEarnings(self):  # not needed
        pass

    def ratePassenger(self):  # not needed
        pass

    def rateDriver(self):  # yes
        pass
