from typing import Dict, List, Tuple


# ============= TreeType Class ================
# This is the Flyweight (intrinsic state)
class TreeType:
    def __init__(self, name: str, color: str, texture: str) -> None:
        # Properties that are common among all trees of this type
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, x: int, y: int) -> None:
        print(f"Drawing {self.name} tree at ({x}, {y})")


# ================ Tree Class =================
# Stores extrinsic state (x, y) and a shared flyweight reference
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        # Attributes that keep on changing
        self.x = x
        self.y = y

        # Shared intrinsic state
        self.tree_type = tree_type

    def draw(self) -> None:
        # Delegates drawing to the shared TreeType
        self.tree_type.draw(self.x, self.y)


# ============ TreeFactory Class ==============
# Ensures TreeType objects are created once and reused
class TreeFactory:
    _tree_type_map: Dict[Tuple[str, str, str], TreeType] = {}

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> TreeType:
        # Key identifies a unique flyweight combination
        key = (name, color, texture)

        # Reuse if present
        if key in TreeFactory._tree_type_map:
            return TreeFactory._tree_type_map[key]

        # Otherwise create and store a new flyweight
        TreeFactory._tree_type_map[key] = TreeType(name, color, texture)
        return TreeFactory._tree_type_map[key]


# ================ Forest Class =================
class Forest:
    def __init__(self) -> None:
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        # Get shared flyweight from the factory
        tree_type = TreeFactory.get_tree_type(name, color, texture)

        # Store only extrinsic state in each Tree
        self.trees.append(Tree(x, y, tree_type))

    def draw(self) -> None:
        for tree in self.trees:
            tree.draw()


# =============== Client Code ==================
def main() -> None:
    forest = Forest()

    # Planting 1 million trees
    for i in range(1_000_000):
        # All trees share the same TreeType flyweight instance
        forest.plant_tree(i, i, "Oak", "Green", "Rough")

    print("Planted 1 million trees.")


if __name__ == "__main__":
    main()
