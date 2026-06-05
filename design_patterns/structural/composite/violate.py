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
        print(f"{indent}Product: {self.name} - \u20b9{self.price}")


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

    print(f"\nTotal Price: \u20b9{total}")


if __name__ == "__main__":
    main()
