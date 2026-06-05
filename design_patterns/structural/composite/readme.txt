C++
|
Java
|
Python
Introduction
Structural design patterns are concerned with the composition of classes and objects. They focus on how to assemble classes and objects into larger structures while keeping these structures flexible and efficient. Composite Pattern is one of the most important structural design patterns. Let's understand in depth.
Composite Pattern
The Composite Pattern is a structural design pattern that allows you to compose objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.
Problem It Solves
The Composite Pattern solves the problem of treating individual objects and groups of objects in the same way. The main problem arises when:
You want to work with a hierarchy of objects.
You want the client code to be agnostic to whether it's dealing with a single object or a collection of them.

Understanding the Problem
Consider you are building the checkout service of an e-commerce application and you take the following approach as shown in the code below.
Code (Without Composite Pattern)
Python


# Represents a single product
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    # Returns the price of this product
    def get_price(self) -> float:
        return self.price

    # Displays this product with indentation
    def display(self, indent: str) -> None:
        print(f"{indent}Product: {self.name} - \u20B9{self.price}")

# Represents a bundle of products (only products, not bundles)
class ProductBundle:
    def __init__(self, bundle_name: str) -> None:
        self.bundle_name = bundle_name
        self.products = []

    # Adds a product to this bundle
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    # Returns total price of products in this bundle
    def get_price(self) -> float:
        total = 0.0
        for product in self.products:
            total += product.get_price()
        return total

    # Displays the bundle and its products
    def display(self, indent: str) -> None:
        print(f"{indent}Bundle: {self.bundle_name}")
        for product in self.products:
            product.display(indent + "  ")

def main() -> None:
    # Individual Items
    book = Product("Book", 500)
    headphones = Product("Headphones", 1500)
    charger = Product("Charger", 800)
    pen = Product("Pen", 20)
    notebook = Product("Notebook", 60)

    # Bundle: Iphone Combo
    iphone_combo = ProductBundle("iPhone Combo Pack")
    iphone_combo.add_product(headphones)
    iphone_combo.add_product(charger)

    # Bundle: School Kit
    school_kit = ProductBundle("School Kit")
    school_kit.add_product(pen)
    school_kit.add_product(notebook)

    # Cart stores mixed types, so client ends up manually branching
    cart = [book, iphone_combo, school_kit]

    print("Cart Details:\n")

    total = 0.0

    # Client has to check what it is dealing with
    for item in cart:
        if isinstance(item, Product):
            item.display("  ")
            total += item.get_price()
        elif isinstance(item, ProductBundle):
            item.display("  ")
            total += item.get_price()

    print(f"\nTotal Price: \u20B9{total}")

if __name__ == "__main__":
    main()
Working of Code
Product class represents a simple item with name and price.
ProductBundle class represents a group of products bundled together.
Both classes have methods to display and return their prices.
In main(), individual products and bundles are created and added to the cart.
The cart holds different types, so the code checks types using isinstance.
Finally, it displays all items and calculates the total price.
Problem in above code
In the above example, the code lacks the structure to treat individual and group items uniformly, i.e., In the current implementation, individual products (Product) and product bundles (ProductBundle) are completely separate types with no shared interface or superclass. This means we cannot write code that treats both uniformly and the logic always has to check which type we're working with.

Other than these, there are some other problems as well:
isinstance is used repeatedly, breaking polymorphism.
Bundle cannot contain another Bundle (no recursive structure).
Client code knows too much about internal types.
As new item types grow, the branching grows too.

Refactored Code Using Composite Pattern
Let's refactor the code using the Composite Pattern. The idea is to create a common interface CartItem for both Product and ProductBundle, allowing us to treat them uniformly.
Python


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
        print(f"{indent}Product: {self.name} - \u20B9{self.price}")

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

    print(f"\nTotal: \u20B9{total}")

if __name__ == "__main__":
    main()
Working of Refactored Code
CartItem interface defines the common methods for both products and bundles.
Product and ProductBundle classes implement the CartItem interface.
The cart now holds a list of CartItem, allowing us to treat both products and bundles uniformly.
The display and price calculation logic is simplified, as we no longer need to check types.

Understanding Leaf and Composite in the Composite Pattern
In the Composite Design Pattern, we categorize components into two main roles:
Leaf (Individual Object): A Leaf is a simple, atomic object in the structure. It does not contain any child components. In our example:
Product is a Leaf.
It represents individual purchasable items like books, phones, pens, etc.
Implements CartItem and provides its own get_price() and display() logic.
Composite (Container of Components): A Composite is a complex object that can hold multiple CartItem objects, including both Leaf and other Composite objects. In our example:
ProductBundle is a Composite.
It can contain Products (leaves) and other ProductBundles (nested composites).
Implements CartItem and delegates actions (get_price() and display()) to its children.

How it Solves the Issues
Uniform Treatment via Shared Interface (CartItem): Now, both Product and ProductBundle implement CartItem, so the cart can contain any of them without special handling.
This eliminates the need for type checking.
Enables Polymorphism: All operations like get_price() and display() are defined in the interface, so they can be called uniformly on both products and bundles.
This simplifies logic and improves code extensibility.
Recursive Composition Made Easy: Bundles can now include other bundles or products seamlessly. This supports deeply nested combos or kits which is a common real-world scenario.
No Code Duplication: The cart-handling logic like computing total and displaying items is written once and works for any CartItem.
This promotes cleaner, DRY (Don't Repeat Yourself) code.

When to Use Composite Pattern
The Composite Pattern is particularly useful when:
You have a hierarchical structure: Use the composite pattern when your objects form a tree-like structure (e.g., folders inside folders, or products inside bundles).
You want to treat individual and groups in the same way: When operations on single items and collections of items should be uniform (e.g., calculating total price, displaying structure).
You want to avoid client-side logic to differentiate leaf and composite: Let polymorphism handle the differences between simple and composite objects, keeping client code clean and maintainable.

Advantages and Disadvantages
Pros:
Uniformity: Treats individual and composite objects in the same way.
Extensible: Easy to add new item types or structures.
Cleaner client code: Reduces complexity for the user of the structure.
Supports OCP (Open/Closed Principle): Add new components without modifying existing code.

Cons:
Violates SRP on scale: Components manage both hierarchy and business logic.
Overkill for flat and simple structures: Adds unnecessary complexity.
Can hide important distinctions: In regulated or sensitive systems, uniform treatment might blur critical differences between types.

Practical Implementation Notes
Python supports dynamic typing, but Composite becomes more maintainable when you make the contract explicit:
Prefer an ABC for clarity:
Using abc.ABC makes it clear which methods every component must implement, even in a dynamically typed language.
Keep recursion predictable:
Composite operations typically recurse. Keep each node's operation small and let the composite orchestrate by delegating to children.
Use type hints in real codebases:
Type hints help IDEs and static analyzers catch mistakes early, especially when nested composites become deep.
Decide whether leaves should support add/remove:
Some teams expose add/remove only on composites. Others include them in the base interface and raise exceptions in leaves. Choose one style and stay consistent.

Class Diagram
The class diagram below illustrates the structure of the Composite Pattern.



21





Facade Pattern - Theory - TUF+