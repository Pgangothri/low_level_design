from abc import ABC, abstractmethod


# Target Interface:
# Standard interface expected by the CheckoutService
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, order_id: str, amount: float) -> None:
        pass


# Concrete implementation of PaymentGateway for PayU
class PayUGateway(PaymentGateway):
    def pay(self, order_id: str, amount: float) -> None:
        print(f"Paid Rs. {amount} using PayU for order: {order_id}")


# Adaptee:
# Existing class with an incompatible interface
class RazorpayAPI:
    def make_payment(self, invoice_id: str, amount_in_rupees: float) -> None:
        print(f"Paid Rs. {amount_in_rupees} using Razorpay for invoice: {invoice_id}")


# Client Class:
# Uses PaymentGateway interface to process payments
class CheckoutService:
    def __init__(self, payment_gateway: PaymentGateway) -> None:
        # Dependency injection to keep service flexible
        self.payment_gateway = payment_gateway

    def checkout(self, order_id: str, amount: float) -> None:
        # Checkout logic uses only the expected interface
        self.payment_gateway.pay(order_id, amount)


def main() -> None:
    # Using PayU payment gateway to process payment
    checkout_service = CheckoutService(PayUGateway())

    # Client uses standardized interface
    checkout_service.checkout("12", 1780)


if __name__ == "__main__":
    main()
