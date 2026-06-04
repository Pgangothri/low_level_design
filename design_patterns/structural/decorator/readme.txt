
Introduction
Structural design patterns are concerned with the composition of classes and objects. They focus on how to assemble classes and objects into larger structures while keeping these structures flexible and efficient. Decorator Pattern is one of the most important structural design patterns. Let's understand in depth.
Decorator Pattern
The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, dynamically at runtime, without affecting the behavior of other objects from the same class.

It wraps an object inside another object that adds new behaviors or responsibilities at runtime, keeping the original object's interface intact.
Real-Life Analogy
Think of a coffee shop:
You order a simple coffee.
Then, you can add milk, add sugar, add whipped cream, etc.
You don't need a whole new drink class for every combination.

Each addition wraps the original and adds something more.
Problem It Solves
It solves the problem of class explosion that occurs when you try to use inheritance to add combinations of behavior. For Example, imagine you have:
A Pizza
A CheesePizza
A CheeseAndOlivePizza
A CheeseAndOliveStuffedPizza

Every combination would need a new subclass as shown in the code below.
Python


# Each combination of pizza requires a new class
class PlainPizza:
    pass

class CheesePizza(PlainPizza):
    pass

class OlivePizza(PlainPizza):
    pass

class StuffedPizza(PlainPizza):
    pass

class CheeseStuffedPizza(CheesePizza):
    pass

class CheeseOlivePizza(CheesePizza):
    pass

class CheeseOliveStuffedPizza(CheeseOlivePizza):
    pass

def main() -> None:
    # Base pizza
    plain_pizza = PlainPizza()

    # Pizzas with individual toppings
    cheese_pizza = CheesePizza()
    olive_pizza = OlivePizza()
    stuffed_pizza = StuffedPizza()

    # Combinations of toppings require separate classes
    cheese_stuffed_pizza = CheeseStuffedPizza()
    cheese_olive_pizza = CheeseOlivePizza()

    # Further combinations increase complexity exponentially
    cheese_olive_stuffed_pizza = CheeseOliveStuffedPizza()

if __name__ == "__main__":
    main()

This quickly becomes unmanageable. Here, the Decorator Pattern comes into play. It lets you compose behaviors using wrappers instead of subclassing.

Solution to Pizza Problem
The Decorator Pattern solves the above discussed Pizza problem. It allows us to add responsibilities (like toppings) to objects dynamically without modifying their structure.

Instead of relying on a rigid class hierarchy, we compose objects using wrappers. This promotes flexibility, scalability, and cleaner code architecture.
Using Decorator Pattern
Python


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
Understanding the Code
The above code:
Defines a Pizza interface that all pizzas (base and decorated) must implement.
Implements two concrete PlainPizza and MargheritaPizza as the base pizzas.
Defines an abstract PizzaDecorator which wraps a Pizza object and forwards method calls to it.
Implements concrete decorators like ExtraCheese, Olives, and StuffedCrust which extend the functionality of the pizza object.
In the main method:
A plain Margherita pizza is created.
It is then wrapped successively with different decorators: ExtraCheese, Olives, and StuffedCrust.
Each decorator adds to the pizza's description and cost.
Finally, the composed pizza's description and total cost are printed.
How Decorator Pattern Solves the Issue
Avoids Class Explosion: You no longer need a separate class for each combination of toppings. Just create new decorators as needed.
Flexible & Scalable: Toppings can be added, removed, or reordered at runtime, offering high customization.
Follows Open/Closed Principle: The base Pizza classes are open for extension (via decorators) but closed for modification.
Cleaner Code Architecture: Composition is used instead of inheritance, resulting in loosely coupled components.
Promotes Reusability: Each topping is a self-contained decorator and can be reused across different pizza compositions.

Key Takeaways
Abstract Classes and Constructors:
In Python, abstract base classes define contracts clearly. Decorators use constructors to receive the wrapped object and store it.
Decorator as Layers:
Each decorator acts like a layer, similar to wrapping a gift box. Every decorator adds behavior on top of the previous one, allowing flexible and dynamic composition of functionality.
Call Stack Analogy:
The decorator chain behaves like stacked layers. Calls go inward through wrappers, and each wrapper contributes to the final output.
Loose Coupling Between Classes:
Using interfaces (ABCs) and composition keeps components loosely coupled and easy to extend.

When Should You Use the Decorator Pattern?
The Decorator Pattern is particularly useful in scenarios where flexibility, modularity, and extensibility are key. Consider using it when:
You need to add responsibilities to objects dynamically:
Decorators allow you to attach additional functionality at runtime.
You want to avoid an explosion of subclasses:
Decorators compose behaviors instead of creating subclasses for every combination.
You want to follow the Open/Closed Principle (OCP):
You add features without editing base classes.
You want reusable and composable behaviors:
Each decorator is a reusable unit that can be stacked.
You need layered, step-by-step enhancements:
Wrapping order can be controlled, making enhancements traceable.

Advantages
A few advantages of using the Decorator Pattern are:
Adheres to the Open/Closed Principle (OCP): Enhancements can be made without modifying existing code.
Runtime Flexibility to Compose Features: Behaviors can be added or removed dynamically.
Avoids Subclass Explosion: Many combinations become possible without creating many subclasses.
Promotes Single Responsibility for Each Add-on: Each decorator focuses on one feature.

Disadvantages
A few trade-offs while using the Decorator Pattern are:
Can Result in Many Small Classes: Each add-on typically becomes its own class.
Stack Trace Debugging is Difficult: Layered wrappers can make debugging harder.
Overhead of Multiple Wrapping Classes: Many wrappers can increase runtime overhead and reduce clarity if overused.
Developers Must Understand Decorator Flow: Wrapping order matters and must be understood.

Practical Implementation Notes
In Python, there is an extra detail that often confuses learners, and a few practices that make the design clearer:
Do not confuse this with Python function decorators:
Python has @decorator syntax for wrapping functions. The design pattern here wraps objects, not functions. The core idea is similar, but the usage is different.
Use ABCs to keep contracts explicit:
Python supports duck typing, but using abc.ABC makes the intent clear and reduces accidental mismatches.
Keep each decorator focused:
One decorator should ideally add one responsibility (like one topping). This keeps composition modular and readable.
Make the wrapper chain easy to understand:
If too many wrappers exist, consider grouping common combinations into factory helpers, while still keeping decorators reusable.

Real-World Use Cases
The Decorator Pattern is widely used in real-life software products to enable dynamic behavior composition without bloating the class hierarchy. Below are practical examples where it plays a critical role:
1. Food Delivery Applications (e.g., Swiggy, Zomato)
Context: Customers can customize food items with add-ons like extra cheese, sauces, toppings, or side dishes.
Role of Decorator Pattern:
Each add-on modifies the base food item's description and price dynamically.
Decorators stack over a base Pizza object to form a final customized item.
This keeps the system open for extension without changing existing base classes.

2. Google Docs or Word Processors
Context: Users can apply text formatting like bold, italic, or underline independently or in combination.
Role of Decorator Pattern:
Each formatting option can be layered as a wrapper to build the final behavior.
This avoids creating separate classes for every formatting combination.

Class Diagram
The class diagram for the Decorator Pattern illustrates the relationship between the component interface, concrete components, and decorators. It shows how decorators extend the functionality of components without modifying their structure.



34





