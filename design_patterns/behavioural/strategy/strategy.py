from typing import Protocol


# ==============================
# Strategy Interface (Protocol)
# ==============================
class MatchingStrategy(Protocol):
    def match(self, rider_location: str) -> None:
        # Common interface method implemented by all strategies
        ...


# ==============================
# Concrete Strategy: Nearest Driver
# ==============================
class NearestDriverStrategy:
    def match(self, rider_location: str) -> None:
        # Print which strategy is being used
        print(f"Matching with the nearest available driver to {rider_location}")

        # Distance-based matching logic
        # For example: compute nearest driver using geo distance


# ==============================
# Concrete Strategy: Airport Queue
# ==============================
class AirportQueueStrategy:
    def match(self, rider_location: str) -> None:
        # Print which strategy is being used
        print(f"Matching using FIFO airport queue for {rider_location}")

        # Match first-in-line driver for airport pickup
        # For example: pop from queue


# ==============================
# Concrete Strategy: Surge Priority
# ==============================
class SurgePriorityStrategy:
    def match(self, rider_location: str) -> None:
        # Print which strategy is being used
        print(f"Matching rider using surge pricing priority near {rider_location}")

        # Prioritize high-surge zones or premium drivers
        # For example: rank drivers by surge multiplier and availability


# ==============================
# Context Class: RideMatchingService
# ==============================
class RideMatchingService:
    def __init__(self, strategy: MatchingStrategy) -> None:
        # Store the current strategy inside the context
        self._strategy = strategy

    def set_strategy(self, strategy: MatchingStrategy) -> None:
        # Swap the current strategy at runtime
        self._strategy = strategy

    def match_rider(self, location: str) -> None:
        # Delegate the matching logic to the current strategy
        self._strategy.match(location)


# ==============================
# Client Code
# ==============================
def main() -> None:
    # Using airport queue strategy
    ride_matching_service = RideMatchingService(AirportQueueStrategy())
    ride_matching_service.match_rider("Terminal 1")

    # Using nearest driver strategy and later switching to surge priority
    ride_matching_service2 = RideMatchingService(NearestDriverStrategy())
    ride_matching_service2.match_rider("Downtown")

    # Switch strategy at runtime
    ride_matching_service2.set_strategy(SurgePriorityStrategy())
    ride_matching_service2.match_rider("Downtown")


if __name__ == "__main__":
    main()
