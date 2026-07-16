import threading


class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        self.lock.acquire()
        self.count += 1  # protected by the lock
        self.lock.release()

    def get_count(self):
        return self.count


counter = SafeCounter()


# Task that bumps the counter 1000 times
def task():
    for _ in range(1000):
        counter.increment()


# Run the same task in two threads
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()

# Expect 2000, but may get less
print(f"Final Count: {counter.get_count()}")
