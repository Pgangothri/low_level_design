# OrderContext class manages the current state of the order
class OrderContext:
    def __init__(self):
        self.currentState = OrderPlacedState()  # default state

    # Method to set a new state for the order
    def setState(self, state):
        self.currentState = state

    # Method to move the order to the next state
    def next(self):
        self.currentState.next(self)

    # Method to cancel the order
    def cancel(self):
        self.currentState.cancel(self)

    # Method to get the current state of the order
    def getCurrentState(self):
        return self.currentState.getStateName()


# OrderState interface defines the behavior of the order states
class OrderState:
    def next(self, context):  # Move to the next state
        pass

    def cancel(self, context):  # Cancel the order
        pass

    def getStateName(self):  # Get the name of the state
        pass


# Concrete states for each stage of the order


# OrderPlacedState handles the behavior when the order is placed
class OrderPlacedState(OrderState):
    def next(self, context):
        context.setState(PreparingState())
        print("Order is now being prepared.")

    def cancel(self, context):
        context.setState(CancelledState())
        print("Order has been cancelled.")

    def getStateName(self):
        return "ORDER_PLACED"


# PreparingState handles the behavior when the order is being prepared
class PreparingState(OrderState):
    def next(self, context):
        context.setState(OutForDeliveryState())
        print("Order is out for delivery.")

    def cancel(self, context):
        context.setState(CancelledState())
        print("Order has been cancelled.")

    def getStateName(self):
        return "PREPARING"


# OutForDeliveryState handles the behavior when the order is out for delivery
class OutForDeliveryState(OrderState):
    def next(self, context):
        context.setState(DeliveredState())
        print("Order has been delivered.")

    def cancel(self, context):
        print("Cannot cancel. Order is out for delivery.")

    def getStateName(self):
        return "OUT_FOR_DELIVERY"


# DeliveredState handles the behavior when the order is delivered
class DeliveredState(OrderState):
    def next(self, context):
        print("Order is already delivered.")

    def cancel(self, context):
        print("Cannot cancel a delivered order.")

    def getStateName(self):
        return "DELIVERED"


# CancelledState handles the behavior when the order is cancelled
class CancelledState(OrderState):
    def next(self, context):
        print("Cancelled order cannot move to next state.")

    def cancel(self, context):
        print("Order is already cancelled.")

    def getStateName(self):
        return "CANCELLED"


# Main method to test the order flow
if __name__ == "__main__":
    order = OrderContext()

    # Display initial state
    print("Current State:", order.getCurrentState())

    # Moving through states
    order.next()  # ORDER_PLACED -> PREPARING
    order.next()  # PREPARING -> OUT_FOR_DELIVERY
    order.cancel()  # Should fail, as order is out for delivery
    order.next()  # OUT_FOR_DELIVERY -> DELIVERED
    order.cancel()  # Should fail, as order is delivered

    # Display final state
    print("Final State:", order.getCurrentState())
