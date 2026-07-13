class Order:
    def __init__(self):
        # Constructor initializes the state to ORDER_PLACED
        self.state = "ORDER_PLACED"

    # Method to cancel the order
    # only allows cancellation if in ORDER_PLACED or PREPARING states
    def cancelOrder(self):
        if self.state == "ORDER_PLACED" or self.state == "PREPARING":
            self.state = "CANCELLED"
            print("Order has been cancelled.")
        else:
            print("Cannot cancel the order now.")

    # Method to move the order to the next state based on its current state
    def nextState(self):
        if self.state == "ORDER_PLACED":
            self.state = "PREPARING"
        elif self.state == "PREPARING":
            self.state = "OUT_FOR_DELIVERY"
        elif self.state == "OUT_FOR_DELIVERY":
            self.state = "DELIVERED"
        else:
            print(f"No next state from: {self.state}")
            return
        print(f"Order moved to: {self.state}")

    # Getter for the state
    def getState(self):
        return self.state


# Main function to test the order flow
if __name__ == "__main__":
    order = Order()

    # Display initial state
    print("Initial State:", order.getState())

    # Moving through states
    order.nextState()  # ORDER_PLACED -> PREPARING
    order.nextState()  # PREPARING -> OUT_FOR_DELIVERY
    order.nextState()  # OUT_FOR_DELIVERY -> DELIVERED

    # Attempting to cancel an order after it is out for delivery
    order.cancelOrder()  # Should not allow cancellation

    # Display final state
    print("Final State:", order.getState())
