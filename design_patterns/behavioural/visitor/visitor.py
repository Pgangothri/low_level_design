
# ======= Element Interface ==========
from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# ======= Concrete elements ===========
class PhysicalProduct(Item):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def accept(self, visitor):
        visitor.visit(self)

# ======= Concrete elements ===========
class DigitalProduct(Item):
    def __init__(self, name, downloadSizeInMB):
        self.name = name
        self.downloadSizeInMB = downloadSizeInMB

    def accept(self, visitor):
        visitor.visit(self)

# ======= Concrete elements ===========
class GiftCard(Item):
    def __init__(self, code, amount):
        self.code = code
        self.amount = amount

    def accept(self, visitor):
        visitor.visit(self)


# ======== Visitor Interface ============
class ItemVisitor(ABC):
    @abstractmethod
    def visit(self, item):
        pass

# ============ Concrete Visitors ==============
class InvoiceVisitor(ItemVisitor):
    def visit(self, item):
        if isinstance(item, PhysicalProduct):
            print(f"Invoice: {item.name} - Shipping to customer")
        elif isinstance(item, DigitalProduct):
            print(f"Invoice: {item.name} - Email with download link")
        elif isinstance(item, GiftCard):
            print(f"Invoice: Gift Card - Code: {item.code}")

# ============ Concrete Visitors ==============
class ShippingCostVisitor(ItemVisitor):
    def visit(self, item):
        if isinstance(item, PhysicalProduct):
            print(f"Shipping cost for {item.name}: Rs. {item.weight * 10}")
        elif isinstance(item, DigitalProduct):
            print(f"{item.name} is digital -- No shipping cost.")
        elif isinstance(item, GiftCard):
            print("GiftCard delivery via email -- No shipping cost.")


# Client Code
def main():
    items = [
        PhysicalProduct("Shoes", 1.2),
        DigitalProduct("Ebook", 100),
        GiftCard("TUF500", 500)
    ]

    invoiceGenerator = InvoiceVisitor()
    shippingCalculator = ShippingCostVisitor()

    for item in items:
        item.accept(invoiceGenerator)
        item.accept(shippingCalculator)
        print()

if __name__ == "__main__":
    main()
