# Implement the solution for Bounded Buffer (producer-consumer)problem using inter process communication techniques-Semaphores
import time
import random

# Define the buffer and its size
buffer = []
buffer_size = 10

# Initialize the semaphore variables
mutex = 1
full = 0
empty = buffer_size

def producer():
    global buffer, mutex, full, empty
    item_count = 0
    while True:
        if mutex == 1 and empty != 0:
            mutex -= 1
            item = random.randint(1, 100)
            buffer.append(item)
            item_count += 1
            full += 1
            empty -= 1
            print(f'Producer produces item {item}, total produced: {item_count}')
            mutex += 1
        else:
            print('Buffer is full!')
        time.sleep(random.random())

def consumer():
    global buffer, mutex, full, empty
    item_count = 0
    while True:
        if mutex == 1 and full != 0:
            mutex -= 1
            item = buffer.pop(0)
            item_count += 1
            full -= 1
            empty += 1
            print(f'Consumer consumes item {item}, total consumed: {item_count}')
            mutex += 1
        else:
            print('Buffer is empty!')
        time.sleep(random.random())

if __name__ == "__main__":
    print("1. Press 1 for Producer\n2. Press 2 for Consumer\n3. Press 3 for Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            producer()
        elif choice == 2:
            consumer()
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
