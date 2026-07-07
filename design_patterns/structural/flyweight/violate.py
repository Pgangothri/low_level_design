from typing import List


# ================ Tree Class =================
class Tree:
    def __init__(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        # Attributes that keep on changing
        self.x = x
        self.y = y

        # Attributes that remain constant
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self) -> None:
        print(f"Drawing tree at ({self.x}, {self.y}) with type {self.name}")


# ================ Forest Class =================
class Forest:
    def __init__(self) -> None:
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        # Creates a fresh Tree object each time
        tree = Tree(x, y, name, color, texture)
        self.trees.append(tree)

    def draw(self) -> None:
        for tree in self.trees:
            tree.draw()


# =============== Client Code ==================
def main() -> None:
    forest = Forest()

    # Planting 1 million trees (all identical in name, color, texture)
    for i in range(1_000_000):
        # Name, color, and texture are duplicated 1 million times
        forest.plant_tree(i, i, "Oak", "Green", "Rough")

    print("Planted 1 million trees.")


if __name__ == "__main__":
    main()
