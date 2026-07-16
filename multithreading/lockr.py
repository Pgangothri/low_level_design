import threading


class SafeCounter:
    def __init__(self):
        self.count = 0
        self.rlock = threading.RLock()

    def increment(self):
        print(f"{threading.current_thread().name} acquired lock in increment()")
        with self.rlock:
            self._do_increment()
        print(f"{threading.current_thread().name} released lock in increment()")

    def _do_increment(self):
        print(
            f"{threading.current_thread().name} acquired lock again in _do_increment()"
        )
        with self.rlock:
            self.count += 1
            print(f"Counter = {self.count}")
        print(f"{threading.current_thread().name} exited _do_increment()")

    def conditional_reset(self, should_reset):
        with self.rlock:
            if should_reset:
                self.count = 0
                print("Counter reset.")
            else:
                print("Reset skipped.")

    def get_count(self):
        with self.rlock:
            return self.count


counter = SafeCounter()


def task():
    for _ in range(5):
        counter.increment()


# Create two threads
t1 = threading.Thread(target=task, name="Thread-1")
t2 = threading.Thread(target=task, name="Thread-2")

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

print("\nFinal Count:", counter.get_count())

# Reset the counter
counter.conditional_reset(True)

print("Count after reset:", counter.get_count())
