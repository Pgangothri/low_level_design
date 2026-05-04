# Class implementing Lazy Loading
class LazySingleton:
    # Object declaration
    __instance = None

    # Private constructor simulation
    def __init__(self):
        if LazySingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        # Declaring it private prevents creation of its object using the new keyword
        LazySingleton.__instance = self

    # Method to get the instance of class
    @staticmethod
    def getInstance():
        # If the object is not created
        if LazySingleton.__instance is None:
            # A new object is created
            LazySingleton()

        # Otherwise the already created object is returned
        return LazySingleton.__instance


lazy = LazySingleton()
two = LazySingleton()
print(two)
print(lazy)
