# Class implementing Eager Loading
class EagerSingleton:
    # Static instance created eagerly
    __instance = None

    # Private constructor simulation
    def __init__(self):
        if EagerSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        # Declaring it private prevents creation of its object using the new keyword
        EagerSingleton.__instance = self

    # Method to get the instance of class
    @staticmethod
    def getInstance():
        return EagerSingleton.__instance  # Always returns the same instance


# Eager initialization (happens at load time)
EagerSingleton._EagerSingleton__instance = EagerSingleton()
print(EagerSingleton.getInstance())  # Output: <__main__.EagerSingleton object at 0x...>
# EagerSingleton._EagerSingleton__instance = EagerSingleton()
# print(EagerSingleton.getInstance())  # Output: <__main__.EagerSingleton object at 0x...>
