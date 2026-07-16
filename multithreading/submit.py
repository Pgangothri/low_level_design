import concurrent.futures
import time


def compute():
    time.sleep(1)
    return 77


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(compute)

    print("Doing other work...")

    result = future.result()  # Blocks until result is ready
    print(f"Result: {result}")

# Executor shuts down automatically on 'with' block exit
