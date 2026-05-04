# Logistics Interface
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def send(self):
        pass


# Class implementing the Logistics Interface
class Road(Logistics):
    def send(self):
        print("Sending by road logic")


# Class implementing the Logistics Interface
class Air(Logistics):
    def send(self):
        print("Sending by air logic")


# Class implementing Logistics Service
class LogisticsService:
    def send(self, mode):
        if mode.lower() == "air":
            logistics = Air()
            logistics.send()
        elif mode.lower() == "road":
            logistics = Road()
            logistics.send()


# Driver code
if __name__ == "__main__":
    service = LogisticsService()
    service.send("Air")
    service.send("Road")
