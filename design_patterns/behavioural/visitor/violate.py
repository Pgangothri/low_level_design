# Class representing a Physical Product
class PhysicalProduct:
    # Method to print invoice for physical product
    def printInvoice(self):
        print("Printing invoice for Physical Product...")

    # Method to calculate shipping cost for physical product
    def calculateShippingCost(self):
        print("Calculating shipping cost for Physical Product...")
        return 10.0  # Example shipping cost


# Class representing a Digital Product
class DigitalProduct:
    # Method to print invoice for digital product
    def printInvoice(self):
        print("Printing invoice for Digital Product...")

    # No shipping cost for digital product


# Class representing a Gift Card Product
class GiftCard:
    # Method to print invoice for gift card
    def printInvoice(self):
        print("Printing invoice for Gift Card...")

    # Method to calculate discount for gift card
    def calculateDiscount(self):
        print("Calculating discount for Gift Card...")
        return 5.0  # Example discount


def main():
    # Create instances of different products
    cart = [PhysicalProduct(), DigitalProduct(), GiftCard()]

    # Loop through cart and perform actions based on product type
    for item in cart:
        if isinstance(item, PhysicalProduct):
            item.printInvoice()
            shippingCost = item.calculateShippingCost()
            print(f"Shipping cost: {shippingCost}\n")
        elif isinstance(item, DigitalProduct):
            item.printInvoice()
            print("No shipping cost for Digital Product.\n")
        elif isinstance(item, GiftCard):
            item.printInvoice()
            discount = item.calculateDiscount()
            print(f"Discount applied: {discount}\n")


if __name__ == "__main__":
    main()
