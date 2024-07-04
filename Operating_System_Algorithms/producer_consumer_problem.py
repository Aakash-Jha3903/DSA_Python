# Program to simulate producer-consumer problem using semaphores.

# Producer consumer problem is a synchronization problem. There is a fixed size buffer where the producer produces items 
# and that is consumed by a consumer process. One solution to the producerconsumer problem uses shared memory. 
# To allow producer and consumer processes to run concurrently, there must be available a buffer of items
# that can be filled by the producer and emptied by the consumer. This buffer will reside in a region of 
# memory that is shared by the producer and consumer processes. The producer and consumer must be synchronized, 
# so that the consumer does not try to consume an item that has not yet been produced.


class ProducerConsumer:
    def __init__(self, buffer_size=10):
        self.buffer = [None] * buffer_size
        self.buffer_size = buffer_size
        self.in_index = 0
        self.out_index = 0

    def produce(self, item):
        if (self.in_index + 1) % self.buffer_size == self.out_index:
            print("Buffer is Full")
        else:
            self.buffer[self.in_index] = item
            print(f"Produced: {item} at index {self.in_index}")
            self.in_index = (self.in_index + 1) % self.buffer_size

    def consume(self):
        if self.in_index == self.out_index:
            print("Buffer is Empty")
        else:
            item = self.buffer[self.out_index]
            print(f"Consumed: {item} from index {self.out_index}")
            self.out_index = (self.out_index + 1) % self.buffer_size

def main():
    pc = ProducerConsumer(buffer_size=10)
    choice = 0

    while choice != 3:
        print("\n1. Produce \t 2. Consume \t 3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the value: "))
            pc.produce(item)
        elif choice == 2:
            pc.consume()
        elif choice == 3:
            print("Exiting...")
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
