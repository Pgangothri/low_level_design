C++
|
Java
|
Python
Builder Pattern
The Builder Pattern is a creational design pattern that separates the construction of a complex object from its representation. This allows you to create different types and representations of an object using the same construction process.
Formal Definition:
"Builder pattern builds a complex object step by step. It separates the construction of a complex object from its representation, so that the same construction process can create different representations."

In simpler terms:
Imagine you're ordering a custom burger. You choose the bun, patty, toppings, sauces, and whether you want it grilled or toasted. The chef follows your instructions step by step to build your custom burger. This is what the Builder Pattern does - it lets you construct complex objects by specifying their parts one at a time, giving you flexibility and control over the object creation process.
Real-life Analogy (Custom Pizza Order)
Think of ordering a pizza online. You select the crust type, size, toppings, cheese, and sauce - all step by step. The pizza shop then builds your pizza according to your selections. Different customers can use the same process to get entirely different pizzas. This is the essence of the Builder Pattern: a structured, step-wise approach to creating customized complex objects.

Understanding the Problem
Imagine you're building a BurgerMeal in your application. A burger must have some mandatory components like: Bun and Patty. And it can also include optional components like: Sides, Toppings, Cheese, and Drink.

Now let’s try to implement this using a traditional constructor approach in Python:
Python


from typing import List, Optional

# Represents a customizable Burger Meal
class BurgerMeal:
    def __init__(self,
                 bun_type: str,
                 patty: str,
                 sides: Optional[str] = None,
                 toppings: Optional[List[str]] = None,
                 cheese: bool = False,
                 drink: Optional[str] = None):
        # Mandatory components
        self.bun_type = bun_type
        self.patty = patty

        # Optional components
        self.sides = sides
        self.toppings = toppings
        self.cheese = cheese
        self.drink = drink

def main():
    # Keyword arguments help readability in Python
    plain_burger = BurgerMeal(bun_type="wheat", patty="veg")

if __name__ == "__main__":
    main()
Issues in Code:
Python is better than Java here because it supports default parameters and keyword arguments. Still, problems show up as the object grows:
Validation becomes scattered:
If you have complex rules, your __init__ becomes large and difficult to maintain.
Mutable state risks:
Many Python objects stay mutable. If you want an immutable, consistent final object, it’s harder without a structured build step.
Too many parameters:
Even with keyword arguments, a constructor with 10-15 optional fields becomes noisy and harder to reason about.
Inconsistent object states:
If the object can be created partially and later modified, it’s easier to end up with invalid or half-configured objects.

So is Builder Pattern useful in Python?
Yes - especially when:
construction involves multiple steps and intermediate validations
you want a clean, fluent creation API
you want to produce an immutable final object (common in LLD and domain modeling)

The Solution
To solve these problems, we use the Builder Pattern. The builder collects configuration step-by-step and returns a final object that is consistent and (optionally) immutable.
Code
Python


from dataclasses import dataclass
from typing import List, Optional

# Final immutable object (frozen=True prevents modifications after creation)
@dataclass(frozen=True)
class BurgerMeal:
    # Required components
    bun_type: str
    patty: str

    # Optional components
    has_cheese: bool
    toppings: List[str]
    side: Optional[str]
    drink: Optional[str]

class BurgerBuilder:
    def __init__(self, bun_type: str, patty: str):
        # Required fields
        self._bun_type = bun_type
        self._patty = patty

        # Optional fields (defaults)
        self._has_cheese = False
        self._toppings: List[str] = []
        self._side: Optional[str] = None
        self._drink: Optional[str] = None

    # Fluent method to set cheese
    def with_cheese(self, has_cheese: bool):
        self._has_cheese = has_cheese
        return self

    # Fluent method to set toppings
    def with_toppings(self, toppings: List[str]):
        self._toppings = toppings
        return self

    # Fluent method to set side
    def with_side(self, side: str):
        self._side = side
        return self

    # Fluent method to set drink
    def with_drink(self, drink: str):
        self._drink = drink
        return self

    # Final build method
    def build(self) -> BurgerMeal:
        # Minimal validation example
        if not self._bun_type or not self._patty:
            raise ValueError("bun_type and patty are mandatory")

        # Return a frozen dataclass instance (immutable)
        return BurgerMeal(
            bun_type=self._bun_type,
            patty=self._patty,
            has_cheese=self._has_cheese,
            toppings=list(self._toppings),
            side=self._side,
            drink=self._drink
        )

def main():
    # Creating burger with only required fields
    plain_burger = BurgerBuilder("wheat", "veg").build()
    print(plain_burger)

    # Burger with cheese only
    burger_with_cheese = BurgerBuilder("wheat", "veg").with_cheese(True).build()
    print(burger_with_cheese)

    # Fully loaded burger
    loaded_burger = (
        BurgerBuilder("multigrain", "chicken")
        .with_cheese(True)
        .with_toppings(["lettuce", "onion", "jalapeno"])
        .with_side("fries")
        .with_drink("coke")
        .build()
    )
    print(loaded_burger)

if __name__ == "__main__":
    main()
Understanding the Code
Builder holds intermediate configuration
The builder stores values step-by-step and only creates the final object in build().
Fluent API Style
Each with_* method returns the builder itself, enabling chaining.
Immutability
The final object is a frozen dataclass, preventing accidental modifications.
Validation at build time
Complex rules can be enforced once inside build(), keeping construction safe.

Why This is Better
Aspect	Constructor Approach	Builder Pattern
Object readability	Okay (keyword args help)	Excellent (fluent, step-wise)
Flexibility	Medium	High
Maintainability	Harder as fields grow	Easy to extend with new options
Safety	Validation often scattered	Central validation + immutable final object

When to Use and When to Avoid the Builder Pattern
When to Use?
Use it when:
The object is complex and requires multiple optional configurations.
You want immutability (common for domain models and config objects).
You need strict validation and want all rules enforced at construction time.
You want a clean creation flow for readability in large codebases.

When to Avoid?
Avoid it when:
The object is small (few fields, simple init).
Keyword arguments already keep it clean and you don’t need extra validation/immutability.

Pros and Cons of Builder Pattern
Pros
Cleaner object creation: construction reads like a story.
Centralized validation: only one place to enforce rules.
Immutable final object: safer and easier to reason about.
Scales well: adding new options is straightforward.

Cons
Extra code: additional builder class is more boilerplate.
Overkill for small objects: unnecessary complexity when defaults are enough.
Two-phase creation: object is only created at build().

Real World Products Using Builder Pattern
1. SQLAlchemy Query Builder Style
Many Python ORMs (like SQLAlchemy) let you build complex queries step-by-step through a fluent API. This is builder-style thinking applied to query construction.
2. argparse Configuration
In many CLI applications, you configure an ArgumentParser step-by-step (add flags/options, set defaults, etc.) before parsing - a builder-like construction flow.
Additional Python Tip
Python often reduces the need for builders because it supports:
keyword arguments (named parameters by default)
dataclasses with defaults
typing + validation libraries (like Pydantic) for safer models

Still, when object creation becomes multi-step or validation-heavy, builder remains a strong choice.

31





Builder Pattern - TUF+