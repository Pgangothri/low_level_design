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


# Adapter Class:
# Converts the interface of RazorpayAPI into PaymentGateway
class RazorpayAdapter(PaymentGateway):
    def __init__(self) -> None:
        # Holding an adaptee instance inside adapter
        self.razorpay_api = RazorpayAPI()

    def pay(self, order_id: str, amount: float) -> None:
        # Translating expected call into adaptee call
        self.razorpay_api.make_payment(order_id, amount)


# Client Class:
# Uses PaymentGateway interface to process payments
class CheckoutService:
    def __init__(self, payment_gateway: PaymentGateway) -> None:
        # Dependency injection makes switching gateways easy
        self.payment_gateway = payment_gateway

    def checkout(self, order_id: str, amount: float) -> None:
        # Client depends only on PaymentGateway interface
        self.payment_gateway.pay(order_id, amount)


def main() -> None:
    # Using Razorpay adapter to process payment
    checkout_service = CheckoutService(RazorpayAdapter())

    # CheckoutService stays unchanged
    checkout_service.checkout("12", 1780)


if __name__ == "__main__":
    main()
