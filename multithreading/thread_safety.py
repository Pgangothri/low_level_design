import threading


# Purchase counter with no protection
class PurchaseCounter:
    def __init__(self):
        # Shared count value
        self.count = 0

    def increment(self):
        # READ current value
        # INCREMENT it
        # WRITE it back
        self.count += 1  # <-- not atomic at Python level, unsafe

    def get_count(self):
        return self.count


counter = PurchaseCounter()


# Task that bumps the counter 1000 times
def task():
    for _ in range(1000):
        counter.increment()


# Run the same task in two threads
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t3 = threading.Thread(target=task)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

# Expect 2000, but may get less
print(f"Final Count: {counter.get_count()}")
