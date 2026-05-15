C++
|
Java
|
Python
Abstract Factory Pattern
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

In simpler terms:
You use it when you have multiple factories, each responsible for producing objects that are meant to work together.
When Should You Use It?
Use of the Abstract Factory Pattern is appropriate in the following scenarios:
When multiple related objects must be created as part of a cohesive set (e.g., a payment gateway and its corresponding invoice generator).
When the type of objects to be instantiated depends on a specific context, such as country, theme, or platform.
When client code should remain independent of concrete product classes.
When consistency across a family of related products must be maintained (e.g., a US payment gateway paired with a US-style invoice).

Real-life Example
Imagine we're building a Checkout Service for our platform TUF Plus:
Bad Design: Hardcoded Object Creation in CheckoutService
This version of the CheckoutService tightly couples business logic with object creation. It works for a simple scenario but quickly becomes problematic as the application scales or needs to support multiple payment gateways and invoice formats.
Python


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
Issues with this design
Tight Coupling:
The CheckoutService directly creates instances of concrete classes, making it dependent on specific implementations.
Violation of the Open/Closed Principle:
Any addition of new payment gateways or invoice types will require modifying the CheckoutService class.
Lack of Extensibility:
Hardcoding limits the ability to support other countries or multiple combinations of payment methods and invoice formats.

Now, let's refactor this code using the Abstract Factory Pattern to improve its design and flexibility.

Improved Design: Abstract Factory Pattern for CheckoutService
This version follows the Abstract Factory Pattern to cleanly separate the creation of PaymentGateway and Invoice objects from the business logic of CheckoutService.
Python


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
How This Code Fixes the Original Issues
Object creation logic was mixed with business logic:
Now moved to separate factory classes like IndiaFactory and USFactory.
Concrete classes were hardcoded in the service:
Replaced with abstractions and created via the factory interface.
Adding a new gateway or invoice type required modifying CheckoutService:
Now, new gateways or invoices can be added by updating a factory or introducing a new factory.
The code was difficult to maintain and scale across regions:
Now easy to scale by plugging in region-specific factories.
Key Benefits of this design
Scalable: Add new countries or payment systems by simply creating new factories.
Clean and Maintainable: CheckoutService does not care what kind of gateway or invoice it's using.
Easy to Test: Each factory can be tested independently.
Follows SOLID Principles: Especially the Open/Closed Principle and Dependency Inversion Principle.

Other Common Approaches in Python
Python allows a few extra approaches that are common in production code:
Duck typing:
In many teams, interfaces are enforced by convention (methods with the right names) rather than explicit ABCs. For teaching LLD, ABCs make the design clearer.
Dependency injection is very natural:
Passing factories (or already created objects) into services is easy, and tests can inject fake factories quickly.
Runtime selection is easier:
Picking a factory based on config or environment variables is straightforward in Python, and still keeps client code clean.
Typed code improves clarity:
Using type hints keeps the pattern readable and prevents misuse when projects grow.

Pros and Cons
Pros of the Abstract Factory Pattern
Encapsulates Object Creation: Centralizes and abstracts the instantiation logic for related objects.
Promotes Consistency Across Products: Ensures that related objects are used together correctly.
Enhances Scalability: Adding new product families can be done by introducing new factory classes.
Supports Open/Closed Principle: Open for extension but closed for modification.
Improves Code Maintainability: Reduces tight coupling between components and specific implementations.
Provides a Layer of Abstraction: Abstracts environment-specific details from the client.

Cons of the Abstract Factory Pattern
Increased Complexity: Adds additional layers (interfaces, factories, product families).
Difficult to Extend Product Families: Adding a new product to an existing family requires updating all factories.
More Boilerplate Code: Requires writing multiple classes even for basic use cases.
Reduced Flexibility in Runtime Decisions: If factories are fixed, switching families at runtime needs extra wiring.

Class Diagram
The class diagram below illustrates the structure of the Abstract Factory Pattern, showing how the various components interact with each other.

Abstract Factory Class Diagram







Abstract Factory - Theory - TUF+