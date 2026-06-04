from abc import ABC, abstractmethod


# =========== Component Interface ============
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# ============= Concrete Components: Base pizza ==============
class PlainPizza(Pizza):
    def get_description(self) -> str:
        return "Plain Pizza"

    def get_cost(self) -> float:
        return 150.00


class MargheritaPizza(Pizza):
    def get_description(self) -> str:
        return "Margherita Pizza"

    def get_cost(self) -> float:
        return 200.00


# ======================== Abstract Decorator ===========================
# Implements Pizza and holds a reference to a Pizza object
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza) -> None:
        # Store the wrapped pizza component
        self.pizza = pizza


# ============ Concrete Decorator: Adds Extra Cheese ================
class ExtraCheese(PizzaDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Extra Cheese"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 40.0


# ============ Concrete Decorator: Adds Olives ================
class Olives(PizzaDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 30.0


# =========== Concrete Decorator: Adds Stuffed Crust Cheese ==============
class StuffedCrust(PizzaDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Stuffed Crust"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 50.0


def main() -> None:
    # Start with a basic Margherita Pizza
    my_pizza: Pizza = MargheritaPizza()

    # Add Extra Cheese by wrapping the existing pizza
    my_pizza = ExtraCheese(my_pizza)

    # Add Olives by wrapping again
    my_pizza = Olives(my_pizza)

    # Add Stuffed Crust by wrapping again
    my_pizza = StuffedCrust(my_pizza)

    # Final Description and Cost
    print(f"Pizza Description: {my_pizza.get_description()}")
    print(f"Total Cost: ₹{my_pizza.get_cost()}")


if __name__ == "__main__":
    main()
