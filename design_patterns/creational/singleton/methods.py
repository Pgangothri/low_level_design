# Synchronised access to the singleton instance
import threading


# Class implementing thread-safe Singleton
class Singleton:
    # Object declaration
    __instance = None

    # Lock for thread safety (similar to Java's 'synchronized')
    __lock = threading.Lock()

    # Private constructor simulation
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    # Thread-safe method to get the instance of class
    @staticmethod
    def getInstance():
        # Only one thread can enter this block at a time
        # This is equivalent to using 'synchronized' in Java
        with Singleton.__lock:  # Synchronized block
            if Singleton.__instance is None:
                Singleton()
        return Singleton.__instance


obj1 = Singleton.getInstance()
obj2 = Singleton.getInstance()

print(obj1 == obj2)  # True

# Double-checked locking (not recommended in Python due to GIL, but shown for completeness)
import threading


# Class implementing double-checked locking Singleton
class Singleton:
    # Object declaration
    __instance = None
    __lock = threading.Lock()

    # Private constructor simulation
    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        Singleton.__instance = self

    # Thread-safe method using double-checked locking
    @staticmethod
    def getInstance():
        if Singleton.__instance is None:  # First check (no lock)
            with Singleton.__lock:
                if Singleton.__instance is None:  # Second check (with lock)
                    Singleton()
        return Singleton.__instance


# Bill pugh Singleton implementation using inner static helper class
# Class implementing Singleton using holder-like lazy initialization
class Singleton:
    # Private constructor simulation
    def __init__(self):
        if hasattr(Singleton, "_created"):
            raise Exception("This class is a singleton!")
        Singleton._created = True


# Function acting like a static holder in Java
def getInstance():
    # This behaves like Java's Holder class:
    # - Singleton instance is not created until getInstance() is first called
    # - The attribute is only added once (lazy initialization)
    # - Thread-safety is not guaranteed unless protected externally
    if not hasattr(getInstance, "_instance"):
        getInstance._instance = Singleton()
    return getInstance._instance
