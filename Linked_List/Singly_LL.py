class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        self.length += 1

    def delete_first_node(self):
        if self.head:
            self.head = self.head.next
            self.length -= 1
        else:
            print("List is empty, no node to delete.")

    def delete_last_node(self):
        if self.head:
            if self.head.next is None:  # for only one node(head)
                self.head = None
                self.length -= 1
                return
            last = self.head
            while last.next.next is not None:
                last = last.next
            last.next = None
            self.length -= 1
        else:
            print("List is empty, no node to delete.")

    def insert_at_position(self, data, pos):
        if pos < 1 or pos > self.length + 1:
            print("Index out of range!")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(pos - 2):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def delete_at_position(self, pos):
        if pos < 1 or pos > self.length:
            print("Index out of range!")
            return
        if pos == 1:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(pos - 2):
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1

    def display(self):
        if self.head:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")
        else:
            print("List is empty.")


def menu():
    linked_list = SinglyLinkedList()
    while True:
        print("\n1. Insert at start")
        print("2. Insert at end")
        print("3. Delete first node")
        print("4. Delete last node")
        print("5. Insert at position")
        print("6. Delete at position")
        print("7. Display Linked-List")
        print("8. Display Length of SLL")
        print("9. Exit\n")

        ch = input("Enter your choice: ")
        
        while ch not  in ('0','1','2','3','4','5','6','7','8','9','10'):
            print("Invalid choice. Please try again.")
            ch = input("Enter your choice: ")
        print("")
        ch = int(ch)
        
        if ch == 1:
            data = int(input("Enter the data: "))
            linked_list.insert_at_start(data)
            print("Node inserted at start.")
        elif ch == 2:
            data = int(input("Enter the data: "))
            linked_list.insert_at_end(data)
            print("Node inserted at end.")
        elif ch == 3:
            linked_list.delete_first_node()
            print("First node deleted.")
        elif ch == 4:
            linked_list.delete_last_node()
            print("Last node deleted.")
        elif ch == 5:
            data = int(input("Enter the data: "))
            pos = int(input("Enter the position: "))
            linked_list.insert_at_position(data, pos)
            print("Node inserted at position.")
        elif ch == 6:
            pos = int(input("Enter the position: "))
            linked_list.delete_at_position(pos)
            print("Node deleted at position.")
        elif ch == 7:
            print("This is your Singly Linked List:")
            linked_list.display()
        elif ch == 8:
            print("Length of SLL is", linked_list.length)
        elif ch == 9:
            print("Dhanyavad ji !")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
