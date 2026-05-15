from abc import ABC, abstractmethod


# Interface representing any payment gateway
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


# Concrete implementation: Razorpay
class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing INR payment via Razorpay: {amount}")


# Concrete implementation: PayU
class PayUGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing INR payment via PayU: {amount}")


# Interface representing invoice generation
class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self) -> None:
        pass


# Concrete invoice implementation for India
class GSTInvoice(Invoice):
    def generate_invoice(self) -> None:
        print("Generating GST Invoice for India.")


# CheckoutService that directly handles object creation (bad practice)
class CheckoutService:
    def __init__(self, gateway_type: str):
        # Stores the gateway type
        self.gateway_type = gateway_type

    def checkout(self, amount: float) -> None:
        # Hardcoded decision logic
        if self.gateway_type == "razorpay":
            payment_gateway = RazorpayGateway()
        else:
            payment_gateway = PayUGateway()

        # Process payment using selected gateway
        payment_gateway.process_payment(amount)

        # Always uses GSTInvoice, even though more types may exist later
        invoice = GSTInvoice()
        invoice.generate_invoice()


def main():
    # Example: Using Razorpay
    razorpay_service = CheckoutService("razorpay")
    razorpay_service.checkout(1500.00)


if __name__ == "__main__":
    main()
