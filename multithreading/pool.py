import concurrent.futures
import time
import threading

def send_email(recipient):
    print(f"Sending email to {recipient} on {threading.current_thread().name}")
    time.sleep(1)  # Simulate delay
    print(f"Email sent to {recipient}")

# Using ThreadPoolExecutor with 10 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(1, 26):
        recipient = f"user{i}@gmail.com"
        executor.submit(send_email, recipient)

# Executor is automatically shut down when exiting the 'with' block,
# waiting for all submitted tasks to complete.
