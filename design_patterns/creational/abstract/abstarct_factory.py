from abc import ABC, abstractmethod


# ========== Interfaces ==========
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self) -> None:
        pass


# ========== India Implementations ==========
class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing INR payment via Razorpay: {amount}")


class PayUGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing INR payment via PayU: {amount}")


class GSTInvoice(Invoice):
    def generate_invoice(self) -> None:
        print("Generating GST Invoice for India.")


# ========== US Implementations ==========
class PayPalGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing USD payment via PayPal: {amount}")


class StripeGateway(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing USD payment via Stripe: {amount}")


class USInvoice(Invoice):
    def generate_invoice(self) -> None:
        print("Generating Invoice as per US norms.")


# ========== Abstract Factory ==========
class RegionFactory(ABC):
    @abstractmethod
    def create_payment_gateway(self, gateway_type: str) -> PaymentGateway:
        pass

    @abstractmethod
    def create_invoice(self) -> Invoice:
        pass


# ========== Concrete Factories ==========
class IndiaFactory(RegionFactory):
    def create_payment_gateway(self, gateway_type: str) -> PaymentGateway:
        # Creates Indian payment gateways
        if gateway_type.lower() == "razorpay":
            return RazorpayGateway()
        if gateway_type.lower() == "payu":
            return PayUGateway()

        raise ValueError(f"Unsupported gateway for India: {gateway_type}")

    def create_invoice(self) -> Invoice:
        # Creates Indian invoice type
        return GSTInvoice()


class USFactory(RegionFactory):
    def create_payment_gateway(self, gateway_type: str) -> PaymentGateway:
        # Creates US payment gateways
        if gateway_type.lower() == "paypal":
            return PayPalGateway()
        if gateway_type.lower() == "stripe":
            return StripeGateway()

        raise ValueError(f"Unsupported gateway for US: {gateway_type}")

    def create_invoice(self) -> Invoice:
        # Creates US invoice type
        return USInvoice()


# ========== Checkout Service ==========
class CheckoutService:
    def __init__(self, factory: RegionFactory, gateway_type: str):
        # Object creation happens via factory, not inside service
        self.payment_gateway = factory.create_payment_gateway(gateway_type)
        self.invoice = factory.create_invoice()

    def complete_order(self, amount: float) -> None:
        # Business logic stays stable
        self.payment_gateway.process_payment(amount)
        self.invoice.generate_invoice()


def main():
    # Using Razorpay in India
    india_checkout = CheckoutService(IndiaFactory(), "razorpay")
    india_checkout.complete_order(1999.0)

    print("---")

    # Using PayPal in US
    us_checkout = CheckoutService(USFactory(), "paypal")
    us_checkout.complete_order(49.99)


if __name__ == "__main__":
    main()
