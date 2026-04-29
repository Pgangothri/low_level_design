if __name__ == "__main__":
    length1 = 10
    width1 = 5
    area1 = length1 * width1
    print("Area1:", area1)

    length2 = 8
    width2 = 4
    area2 = length2 * width2
    print("Area2:", area2)

    # DRY Violation: Repeated code for calculating area of rectangles. This can be refactored into a function to avoid code duplication and improve maintainability.


class AreaCalculator:
    @staticmethod
    def calculateArea(length, width):
        return length * width


if __name__ == "__main__":
    area1 = AreaCalculator.calculateArea(10, 5)
    area2 = AreaCalculator.calculateArea(8, 4)

    print("Area1:", area1)
    print("Area2:", area2)
