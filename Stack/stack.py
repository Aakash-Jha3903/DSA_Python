class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        # return self.stack == []
        return len(self.stack) == 0

    def pushStack(self, data):
        self.stack.append(data)
        print(f"Pushed {data} onto the stack.")

    def popStack(self):
        if self.isEmpty():
            print("Underflow! (Stack is empty, nothing to pop.)")
        else:
            print(f"Popped {self.stack.pop()} from the stack.")

    def peekStack(self):
        if self.isEmpty():
            print("Stack is empty, nothing to peek.")
        else:
            print(f"Top element is {self.stack[-1]} ")

    def displayStack(self):
        if self.isEmpty():
            print("Stack is empty, nothing to display.")
        else:
            # print(self.stack)
            print("Stack elements are:")
            for data in reversed(self.stack):
                print(data)


def menu():
    stack = Stack()
    while True:
        print("\n0. Create a Stack of n elements ")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit\n")

        ch = input("Enter your choice: ")
        while ch not in ('0', '1', '2', '3', '4', '5'):
            print("Invalid choice. Please try again.")
            ch = input("Enter your choice: ")
        print("")
        ch = int(ch)

        if ch == 0:
            n = int(input('Enter the number of elements : '))
            print("Enter the elements : ")
            for _ in range(n):
                ele = int(input(f"Enter the element [{_}]  : "))
                stack.pushStack(ele)        
                
        elif ch == 1:
            data = int(input("Enter the data to push: "))
            stack.pushStack(data)
        elif ch == 2:
            stack.popStack()
        elif ch == 3:
            stack.peekStack()
        elif ch == 4:
            stack.displayStack()
        elif ch == 5: 
            print("Dhanyavad ji , fhir milengee ....")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()