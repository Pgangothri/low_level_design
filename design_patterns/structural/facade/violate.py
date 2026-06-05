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


def main() -> None:
    # Booking a movie ticket manually (without a facade)

    # Step 1: Make payment
    payment_service = PaymentService()
    payment_service.make_payment("user123", 500)

    # Step 2: Reserve seat
    seat_reservation_service = SeatReservationService()
    seat_reservation_service.reserve_seat("movie456", "A10")

    # Step 3: Send booking confirmation via email
    notification_service = NotificationService()
    notification_service.send_booking_confirmation("user@example.com")

    # Step 4: Add loyalty points to user's account
    loyalty_points_service = LoyaltyPointsService()
    loyalty_points_service.add_points("user123", 50)

    # Step 5: Generate the ticket
    ticket_service = TicketService()
    ticket_service.generate_ticket("movie456", "A10")


if __name__ == "__main__":
    main()
