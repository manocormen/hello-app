import time

start = time.time()

while True:
    print("Hello, World!")
    now = time.time()
    print(f"Time elapsed: {round(now - start)}")
    time.sleep(1)
