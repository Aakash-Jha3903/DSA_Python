import time


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head is None
    
    def display(self):
        if self.head:
            print("This is your Stack:")
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")
        else:
            print("Stack is empty.") 
            
    def pushStack(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        print("Node inserted.")
        time.sleep(2)
        self.display()

    def popStack(self):
        if self.head:
            print(f"{self.head} is popped")
            self.head = self.head.next
            self.length -= 1
            self.display()
        else:
            print("Stack is empty.")
    
    def peek(self):
        if self.head:
            print(self.head.data)
        else:
            print("Stack is empty.")


def menu():
    stack = Stack()
    while True:
        print("\nMenu:")
        print("0. Create a Stack of n Nodes")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        while choice not in ('0', '1', '2', '3', '4', '5'):
            print("Invalid choice. Please try again.")
            choice = input("Enter your choice: ")
        print("")
        choice = int(choice)

        if choice == 0:
            n = int(input('Enter the number of elements : '))
            print("Enter the elements : ")
            for _ in range(n):
                ele = int(input(f"Enter the element [{_}]  : "))
                stack.pushStack(ele)        
                
        elif choice == 1:
            data = int(input("Enter data to push: "))
            stack.pushStack(data)
        elif choice == 2:
            stack.popStack()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Dhanyavad ji , fhir milengee ....")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()