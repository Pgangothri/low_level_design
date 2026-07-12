# Class implementing Ride Matching Service (naive approach)
class RideMatchingService:
    def match_rider(self, rider_location: str, matching_type: str) -> None:
        # Choose strategy using hardcoded conditionals
        if matching_type == "NEAREST":
            # Find nearest driver
            print(f"Matching rider at {rider_location} with nearest driver.")
        elif matching_type == "SURGE_PRIORITY":
            # Match based on surge area logic
            print(
                f"Matching rider at {rider_location} based on surge pricing priority."
            )
        elif matching_type == "AIRPORT_QUEUE":
            # Use FIFO-based airport queue logic
            print(f"Matching rider at {rider_location} from airport queue.")
        else:
            print("Invalid matching strategy provided.")


def main() -> None:
    # Create the service
    service = RideMatchingService()

    # Try different strategies
    service.match_rider("Downtown", "NEAREST")
    service.match_rider("City Center", "SURGE_PRIORITY")
    service.match_rider("Airport Terminal 1", "AIRPORT_QUEUE")


if __name__ == "__main__":
    main()
