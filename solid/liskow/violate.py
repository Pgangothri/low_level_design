# Rectangle class
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def setWidth(self, w):
        self.width = w

    def setHeight(self, h):
        self.height = h

    def getArea(self):
        return self.width * self.height


# Square class extending the Rectangle class
class Square(Rectangle):
    def setWidth(self, w):
        self.width = w
        self.height = w  # makes it a square

    def setHeight(self, h):
        self.height = h
        self.width = h  # makes it a square


# Method to print the area of the given rectangle object
def printArea(r):
    r.setWidth(5)
    r.setHeight(10)
    print(r.getArea())  # Expected: 50 but Actual: 100


# Main section
if __name__ == "__main__":
    # Replacing object of Rectangle class with Square class
    r = Square()

    # Method call to print the area of the rectangle
    printArea(r)
