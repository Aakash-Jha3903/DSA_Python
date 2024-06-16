import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def display(self):
        if self.isEmpty():
            print("Queue is Empty ! \nNothing to display")
        else:
            print("This is your Queue")
            current = self.front
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def Enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{self.rear.data} is enqueued into the Queue.")
        time.sleep(1)
        self.display()

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty ! \nNothing to display")
        else:
            print(f"{self.front.data} is dequeued from the Queue.")
            self.front = self.front.next
            if self.front is None:  # it "was" the one and last node
                self.rear = None
            self.display()


def menu():
    queue = Queue()
    while True:
        print("\n0. Create a Queue of n elements ")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit\n")

        ch = input("Enter your choice: ")
        while ch not in ('0', '1', '2', '3', '4'):
            print("Invalid choice. Please try again.")
            ch = input("Enter your choice: ")
        print("")
        ch = int(ch)

        if ch == 0:
            n = int(input('Enter the number of elements : '))
            print("Enter the elements : ")
            for _ in range(n):
                ele = int(input(f"Enter the element [{_}]  : "))
                queue.Enqueue(ele)
        elif ch == 1:
            data = int(input("Enter the data to push: "))
            queue.Enqueue(data)
        elif ch == 2:
            queue.Dequeue()
        elif ch == 3:
            queue.display()
        elif ch == 4:
            print("Dhanyavad ji , fhir milengee ....")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
