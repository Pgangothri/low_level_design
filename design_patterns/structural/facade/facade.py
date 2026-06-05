# Service class responsible for handling payments
class PaymentService:
    def make_payment(self, account_id: str, amount: float) -> None:
        print(f"Payment of \u20b9{amount} successful for account {account_id}")


# Service class responsible for reserving seats
class SeatReservationService:
    def reserve_seat(self, movie_id: str, seat_number: str) -> None:
        print(f"Seat {seat_number} reserved for movie {movie_id}")


# Service class responsible for sending notifications
class NotificationService:
    def send_booking_confirmation(self, user_email: str) -> None:
        print(f"Booking confirmation sent to {user_email}")


# Service class for managing loyalty/reward points
class LoyaltyPointsService:
    def add_points(self, account_id: str, points: int) -> None:
        print(f"{points} loyalty points added to account {account_id}")


# Service class for generating movie tickets
class TicketService:
    def generate_ticket(self, movie_id: str, seat_number: str) -> None:
        print(f"Ticket generated for movie {movie_id}, Seat: {seat_number}")


# ========== The MovieBookingFacade class ==============
class MovieBookingFacade:
    def __init__(self) -> None:
        # Initialize all the subsystem services inside the facade
        self.payment_service = PaymentService()
        self.seat_reservation_service = SeatReservationService()
        self.notification_service = NotificationService()
        self.loyalty_points_service = LoyaltyPointsService()
        self.ticket_service = TicketService()

    # Method providing a simplified interface for booking a movie ticket
    def book_movie_ticket(
        self,
        account_id: str,
        movie_id: str,
        seat_number: str,
        user_email: str,
        amount: float,
    ) -> None:
        # Step 1: Make payment
        self.payment_service.make_payment(account_id, amount)

        # Step 2: Reserve seat
        self.seat_reservation_service.reserve_seat(movie_id, seat_number)

        # Step 3: Generate ticket
        self.ticket_service.generate_ticket(movie_id, seat_number)

        # Step 4: Add loyalty points
        self.loyalty_points_service.add_points(account_id, 50)

        # Step 5: Send confirmation
        self.notification_service.send_booking_confirmation(user_email)

        # Indicate successful completion of the entire booking process
        print("Movie ticket booking completed successfully!")


def main() -> None:
    # Booking a movie ticket using the facade
    movie_booking_facade = MovieBookingFacade()

    # Client calls a single high-level API instead of coordinating multiple services
    movie_booking_facade.book_movie_ticket(
        "user123", "movie456", "A10", "user@example.com", 500
    )


if __name__ == "__main__":
    main()
