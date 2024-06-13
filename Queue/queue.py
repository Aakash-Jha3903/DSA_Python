class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)
        print(data, "added to queue")
    
    def dequeue(self):
        if not self.isEmpty():
            print(f"{self.queue.pop(0)} is dequeued.")  # 0 index
        else:
            print("Queue is empty")
        
    
    def display(self):
        if not self.isEmpty():
            print(self.queue)
        else:
            print("Queue is empty")


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
                queue.enqueue(ele)                
        elif ch == 1:
            data = int(input("Enter the data to push: "))
            queue.enqueue(data)
        elif ch == 2:
            queue.dequeue()
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