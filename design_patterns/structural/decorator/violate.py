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
