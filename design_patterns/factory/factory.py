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


# Factory Class taking care of Logistics
class LogisticsFactory:
    @staticmethod
    def get_logistics(mode):
        if mode.lower() == "air":
            return Air()
        elif mode.lower() == "road":
            return Road()
        else:
            raise ValueError(f"Unknown logistics mode: {mode}")


# Class implementing the Logistics Services
class LogisticsService:
    def send(self, mode):
        # Using the Logistics Factory to get the desired object based on the mode
        logistics = LogisticsFactory.get_logistics(mode)
        logistics.send()


# Driver Code
if __name__ == "__main__":
    service = LogisticsService()
    service.send("Air")
    service.send("Road")
