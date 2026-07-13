# Abstract class defining the SupportHandler
class SupportHandler:
    def __init__(self):
        self.next_handler = None

    # Method to set the next handler in the chain
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    # Abstract method to handle the request
    def handle_request(self, request_type):
        raise NotImplementedError


# Concrete Handler for General Support
class GeneralSupport(SupportHandler):
    def handle_request(self, request_type):
        if request_type.lower() == "general":
            print("GeneralSupport: Handling general query")
        elif self.next_handler:
            self.next_handler.handle_request(request_type)


# Concrete Handler for Billing Support
class BillingSupport(SupportHandler):
    def handle_request(self, request_type):
        if request_type.lower() == "refund":
            print("BillingSupport: Handling refund request")
        elif self.next_handler:
            self.next_handler.handle_request(request_type)


# Concrete Handler for Technical Support
class TechnicalSupport(SupportHandler):
    def handle_request(self, request_type):
        if request_type.lower() == "technical":
            print("TechnicalSupport: Handling technical issue")
        elif self.next_handler:
            self.next_handler.handle_request(request_type)


# Concrete Handler for Delivery Support
class DeliverySupport(SupportHandler):
    def handle_request(self, request_type):
        if request_type.lower() == "delivery":
            print("DeliverySupport: Handling delivery issue")
        elif self.next_handler:
            self.next_handler.handle_request(request_type)
        else:
            print("DeliverySupport: No handler found for request")


# Client Code
if __name__ == "__main__":
    general = GeneralSupport()
    billing = BillingSupport()
    technical = TechnicalSupport()
    delivery = DeliverySupport()

    # Setting up the chain: general -> billing -> technical -> delivery
    general.set_next_handler(billing)
    billing.set_next_handler(technical)
    technical.set_next_handler(delivery)

    # Testing the chain of responsibility with different request types
    general.handle_request("refund")
    general.handle_request("delivery")
    general.handle_request("unknown")
