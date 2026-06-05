from abc import ABC, abstractmethod
from typing import List


# Interface for items that can be added to the cart
class CartItem(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def display(self, indent: str) -> None:
        pass


# Product class implementing CartItem (Leaf)
class Product(CartItem):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    # Returns price of the product
    def get_price(self) -> float:
        return self.price

    # Displays product details
    def display(self, indent: str) -> None:
        print(f"{indent}Product: {self.name} - \u20b9{self.price}")


# ProductBundle implementing CartItem (Composite)
class ProductBundle(CartItem):
    def __init__(self, bundle_name: str) -> None:
        self.bundle_name = bundle_name

        # Store children as CartItem so bundle can contain products and other bundles
        self.items: List[CartItem] = []

    # Adds an item (Product or ProductBundle) to this bundle
    def add_item(self, item: CartItem) -> None:
        self.items.append(item)

    # Returns total price of all children
    def get_price(self) -> float:
        total = 0.0

        # Each child knows how to compute its price
        for item in self.items:
            total += item.get_price()

        return total

    # Displays bundle and recursively displays children
    def display(self, indent: str) -> None:
        print(f"{indent}Bundle: {self.bundle_name}")

        # Each child knows how to display itself
        for item in self.items:
            item.display(indent + "  ")


def main() -> None:
    # Individual Products (Leaf nodes)
    book = Product("Atomic Habits", 499)
    phone = Product("iPhone 15", 79999)
    earbuds = Product("AirPods", 15999)
    charger = Product("20W Charger", 1999)

    # Combo Deal (Composite node)
    iphone_combo = ProductBundle("iPhone Essentials Combo")
    iphone_combo.add_item(phone)
    iphone_combo.add_item(earbuds)
    iphone_combo.add_item(charger)

    # Back to School Kit (Composite node)
    school_kit = ProductBundle("Back to School Kit")
    school_kit.add_item(Product("Notebook Pack", 249))
    school_kit.add_item(Product("Pen Set", 99))
    school_kit.add_item(Product("Highlighter", 149))

    # Nested bundles become easy with a composite structure
    mega_bundle = ProductBundle("Mega Festival Bundle")
    mega_bundle.add_item(book)
    mega_bundle.add_item(iphone_combo)
    mega_bundle.add_item(school_kit)

    # Cart can now store a single type safely
    cart: List[CartItem] = [book, iphone_combo, school_kit, mega_bundle]

    # Display cart
    print("Your Amazon Cart:")
    total = 0.0

    # No type checking is needed, polymorphism handles everything
    for item in cart:
        item.display("  ")
        total += item.get_price()

    print(f"\nTotal: \u20b9{total}")


if __name__ == "__main__":
    main()
