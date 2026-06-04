Theory

Discussion
C++
|
Java
|
Python
Introduction
Structural design patterns are concerned with the composition of classes and objects. They focus on how to assemble classes and objects into larger structures while keeping these structures flexible and efficient. Adapter Pattern is one of the most important structural design patterns. Let's understand in depth.
Adapter Pattern
The Adapter Pattern allows incompatible interfaces to work together by acting as a translator or wrapper around an existing class. It converts the interface of a class into another interface that a client expects.

It acts as a bridge between the Target interface (expected by the client) and the Adaptee (an existing class with a different interface). This structural wrapping enables integration and compatibility across diverse systems.
Real-Life Analogy
Imagine traveling from India to Europe. Your mobile charger doesn't fit into European sockets. Instead of buying a new charger, you use a plug adapter. The adapter allows your charger (with its Indian plug) to fit the European socket, enabling charging without modifying either the socket or the charger.
Problem It Solves
Interface incompatibility between classes.
Reusability of existing classes without modifying their source code.
Enables systems to communicate that otherwise couldn't due to differing method signatures.

Similarly, the Adapter Pattern allows objects with incompatible interfaces to collaborate by introducing an adapter.

Real-Life Coding Example
Let's consider a scenario where we are implementing the Payment Gateway System. And we have two different payment methods: PayU and Razorpay. While the PayU gateway already conforms to this interface, Razorpay follows a different structure as shown in the code below.
Using Incompatible Interface (Without Adapter)
Python


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
Understanding the Issues
CheckoutService expects any payment provider to implement PaymentGateway.
PayUGateway matches the required interface and works.
RazorpayAPI uses a different method (make_payment) and cannot be passed directly.
Due to this mismatch, the Razorpay integration fails without changing code structure.

To solve this without modifying existing code, we use the Adapter Pattern to make RazorpayAPI compatible with the expected interface.

Using Adapter Pattern
Python


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

Here, we created an adapter class RazorpayAdapter that implements PaymentGateway. The adapter internally uses RazorpayAPI and translates calls from the expected interface to the existing implementation.

This allows us to integrate Razorpay seamlessly with CheckoutService without modifying either class.

When to Use Adapter Pattern
The Adapter Pattern is ideal in scenarios where you're trying to integrate components that were not originally designed to work together. It proves especially useful when:
You need to use an existing class, but its interface does not match the one your system expects.
You want to reuse legacy code without modifying its internal structure.
You're integrating third-party APIs or external services into your application.

In such cases, the Adapter Pattern serves as a bridge, allowing seamless compatibility without altering existing codebases.

Advantages and Disadvantages
Like any design pattern, the Adapter Pattern comes with its own set of pros and cons:
Pros:
Code Reusability: Encourages the reuse of existing classes without changing their implementation.
Code Extensibility: Makes systems more flexible and adaptable to change.
Minimal Changes to Client Code: Enables integration without requiring modifications to existing client logic.
Simplifies Third-party Integration: Makes it easier to incorporate external services and APIs.

Cons:
Adds an Extra Layer of Abstraction: Can introduce unnecessary complexity if not used judiciously.
Overuse Can Obscure System Design: Excessive use of adapters might make the architecture harder to understand and maintain.

Practical Implementation Notes
While implementing Adapter Pattern in Python, a few things make the approach cleaner and production-friendly:
Prefer composition over inheritance for the adaptee:
Keep a reference to the adaptee inside the adapter and translate calls.
Be careful with dynamic typing:
Python allows duck typing, but using ABC (abstract base classes) keeps contracts explicit and easier to reason about.
Adapters are commonly used as thin wrappers:
Python adapters often just rename methods and reshape data formats.
Keep translation logic inside adapter:
Mapping order_id to invoice_id or converting currency belongs in the adapter, not in client code.

Real Product Use Cases
The Adapter Pattern is not just a theoretical concept. It plays a crucial role in real-world software products and systems. Many enterprise-level applications rely on this pattern to integrate with third-party tools, legacy systems, and platform-specific APIs. Below are some common and impactful use cases:
1. Payment Gateways
Scenario: Different payment providers expose their own APIs with varying method names, parameters, and response formats.

Adapter Use: By implementing a common PaymentGateway interface and creating adapters for each provider, businesses can switch or support multiple gateways without rewriting business logic.
2. Logging Frameworks
Scenario: Applications may use different logging backends or custom wrappers.

Adapter Use: A wrapper can keep a consistent method like info() and internally call another library or remote logger.
3. Cloud Providers and SDKs
Scenario: Cloud platforms offer similar services but expose them differently.

Adapter Use: An adapter layer abstracts cloud operations behind a common interface, enabling switching providers easily.

Class Diagram


The class diagram below illustrates the Adapter Pattern. The PaymentGateway interface is the target interface, while RazorpayAPI is the adaptee. The RazorpayAdapter acts as a bridge, allowing the client to interact with the adaptee through the target interface.
Adapter Pattern - Theory - TUF+