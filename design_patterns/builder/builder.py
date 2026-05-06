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
            drink=self._drink,
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
