class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(item, "added to the front of deque")

    def add_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        print(item, "added to the rear of deque")

    def remove_front(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            removed_data = self.front.data
            if self.front == self.rear:  # Only one element
                self.front = self.rear = None
            else:
                self.front = self.front.next
                self.front.prev = None
            print(f"{removed_data} removed from the front of deque")

    def remove_rear(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            removed_data = self.rear.data
            if self.front == self.rear:  # Only one element
                self.front = self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            print(f"{removed_data} removed from the rear of deque")

    def display(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            current = self.front
            deque_elements = []
            while current:
                deque_elements.append(current.data)
                current = current.next
            print("Deque contents:", deque_elements)

def menu():
    deque = Deque()
    while True:
        print("\n0. Create a Deque with n elements ")
        print("1. Add to front")
        print("2. Add to rear")
        print("3. Remove from front")
        print("4. Remove from rear")
        print("5. Display Deque")
        print("6. Exit\n")

        ch = input("Enter your choice: ")
        while ch not in ('0', '1', '2', '3', '4', '5', '6'):
            print("Invalid choice. Please try again.")
            ch = input("Enter your choice: ")
        print("")
        ch = int(ch)

        if ch == 0:
            n = int(input('Enter the number of elements: '))
            print("Enter the elements: ")
            for _ in range(n):
                ele = int(input(f"Enter element [{_+1}]: "))
                deque.add_rear(ele)                
        elif ch == 1:
            data = int(input("Enter the data to add to the front: "))
            deque.add_front(data)
        elif ch == 2:
            data = int(input("Enter the data to add to the rear: "))
            deque.add_rear(data)
        elif ch == 3:
            deque.remove_front()
        elif ch == 4:
            deque.remove_rear()
        elif ch == 5:
            deque.display()
        elif ch == 6: 
            print("Dhanyavad ji , fhir milengee ....")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
