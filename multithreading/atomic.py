import threading


class AtomicCounter:
    """A thread-safe integer counter backed by a Lock."""

    def __init__(self, initial=0):
        self._value = initial
        self._lock = threading.Lock()

    def increment(self):
        """Atomically add 1 to the counter."""
        with self._lock:
            # Step 1 - read the current value (under lock)
            prev = self._value

            # Step 2 - compute the desired next value
            next_val = prev + 1

            # Step 3 - write back (under the same lock)
            # No other thread can interleave these steps
            self._value = next_val
        return next_val

    def get(self):
        """Thread-safe read."""
        with self._lock:
            return self._value


# Usage
counter = AtomicCounter()


def task():
    for _ in range(1000):
        counter.increment()


t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final Count: {counter.get()}")  # Always 2000
