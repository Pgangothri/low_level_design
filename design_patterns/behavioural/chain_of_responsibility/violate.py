# SupportService class: Handles different types of support requests
class SupportService:
    # Method to handle the support request based on the type of issue
    def handle_request(self, type):
        if type == "general":
            print("Handled by General Support")
        elif type == "refund":
            print("Handled by Billing Team")
        elif type == "technical":
            print("Handled by Technical Support")
        elif type == "delivery":
            print("Handled by Delivery Team")
        else:
            print("No handler available")


# Main function: Entry point to test the chain of responsibility pattern
if __name__ == "__main__":
    # Create an instance of SupportService
    support_service = SupportService()

    # Test with different types of requests
    support_service.handle_request("general")
    support_service.handle_request("refund")
    support_service.handle_request("technical")
    support_service.handle_request("delivery")
    support_service.handle_request("unknown")
