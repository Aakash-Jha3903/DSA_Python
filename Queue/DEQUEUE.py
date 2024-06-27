class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)
        print(item, "added to the front of deque")

    def add_rear(self, item):
        self.items.append(item)
        print(item, "added to the rear of deque")

    def remove_front(self):
        if not self.is_empty():
            print(f"{self.items.pop(0)} removed from the front of deque")
        else:
            print("Deque is empty")

    def remove_rear(self):
        if not self.is_empty():
            print(f"{self.items.pop()} removed from the rear of deque")
        else:
            print("Deque is empty")

    def display(self):
        if not self.is_empty():
            print("Deque contents:", self.items)
        else:
            print("Deque is empty")

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
