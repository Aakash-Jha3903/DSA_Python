# Created by Aakash Jha
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def display(self):
        if self.head:
            print("This is your Circular Linked List:")
            n = self.length
            temp = self.head
            for _ in range(n):
                print(temp.data, end=" -> ")
                temp = temp.next
            print("head(again)")
        else:
            print("Linked list is empty !")
        time.sleep(2)

    def Create_N_nodes(self, n, data_list):
        if self.head:
            print("Circular Linked List already exists!")
            time.sleep(2)
            self.display()
            return
        for i in data_list:
            if self.head is None:  # first-time(edge case)
                self.head = Node(i)
                self.head.next = self.head  # circular Linked list
                temp = self.head
                self.length += 1
            else:
                new_node = Node(i)
                temp.next = new_node
                new_node.next = self.head
                temp = new_node  # keep track of the last node
                self.length += 1
        print("Circular Linked List created successfully!")
        print("This is your Circular Linked List:")
        self.display()  # self.....

    def insert_at_start(self, data):
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            temp = self.head
            for _ in range(self.length + 1):
                temp = temp.next
            temp.next = self.head
            self.length += 1
            print("Node inserted at start.")
            time.sleep(2)
            self.display()
        else:
            self.head = Node(data)
            self.head.next = self.head
            self.length += 1
            print("Node inserted at start.")
            time.sleep(2)
            self.display()

    def insert_at_end(self, data):
        if self.head:
            new_node = Node(data)
            temp = self.head
            for _ in range(self.length):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.length += 1
            print("Node inserted at end.")
            time.sleep(2)
            self.display()
        else:
            self.head = Node(data)
            self.head.next = self.head
            self.length += 1
            print("Node inserted at end.")
            time.sleep(2)
            self.display()

    def delete_first_node(self):
        if self.head:
            if self.length == 1:  # (imp.) Check if it's the only node
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:  # Traverse to the last node
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head  # Link last node to new head
            self.length -= 1
            print("First node deleted.")
            time.sleep(2)
            self.display()
        else:
            print("List is empty, no node to delete.")
            time.sleep(2)

    def delete_last_node(self):
        if self.head:
            if self.length == 1:  # (imp.) Check if it's the only node
                self.head = None
            else:
                temp = self.head
                while temp.next.next != self.head:  # Traverse to the second last node
                    temp = temp.next
                temp.next = self.head  # Remove last node by linking to head
            self.length -= 1
            print("Last node deleted.")
            time.sleep(2)
            self.display()
        else:
            print("List is empty, no node to delete.")
            time.sleep(2)

    def insert_at_position(self, data, pos):
        # (imp.) [+1 , OR-operator] Corrected boundary condition
        if pos < 1 or pos > self.length + 1:
            print("Index out of range!")
            time.sleep(2)
            return

        new_node = Node(data)
        if pos == 1:
            if not self.head:  # (v.imp.) if CLL is empty (1st insertion)!!
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:  # Traverse to the last node (due to Circular LL)
                    temp = temp.next
                new_node.next = self.head
                self.head = new_node
                temp.next = self.head  # Link last node to new head !!

        else:
            temp = self.head
            for _ in range(pos - 2):  # Traverse to the node before the insertion point
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        print(f"Node inserted at position {pos}.")
        self.display()

    def delete_at_position(self, pos):
        if pos < 1 or pos > self.length:
            print("Index out of range!")
            return
        if self.head:
            if pos == 1:
                if self.length == 1:  # Check if it's the only node
                    self.head = None
                else:
                    temp = self.head
                    while temp.next != self.head:  # Traverse to the last node
                        temp = temp.next
                    self.head = self.head.next
                    temp.next = self.head  # Link last node to new head
            else:
                temp = self.head
                for _ in range(pos - 2):  # Traverse to the node before the deletion point
                    temp = temp.next
                temp.next = temp.next.next  # Remove the node by linking to the next of next node
            self.length -= 1
            print(f"Node at position {pos} deleted.")
            self.display()
        else:
            print("List is empty, no node to delete.")
            time.sleep(2)

    def delete_entire_list(self):
        if self.head:
            self.head = None
            self.length = 0
            print("The entire linked list has been deleted.")
        else:
            print("List is empty, no node to delete.")
        time.sleep(2)


def menu():
    linked_list = CircularLinkedList()
    while True:
        print("\n0. Create a Circular linked list with N nodes")
        print("1. Insert at start")
        print("2. Insert at end")
        print("3. Delete first node")
        print("4. Delete last node")
        print("5. Insert at position")
        print("6. Delete at position")
        print("7. Display Linked-List")
        print("8. Display Length of CLL")
        print("9. Delete Entire Circular linked list")
        print("10. Exit\n")

        ch = input("Enter your choice: ")
        
        while ch not  in ('0','1','2','3','4','5','6','7','8','9','10'):
            print("Invalid choice. Please try again.")
            ch = input("Enter your choice: ")
        print("")
        ch = int(ch)
        
        if ch == 0:
            n = int(input("Enter the number of nodes: "))
            if n <= 0:
                print("Enter a natural number!")
                print("Try again")
                time.sleep(2)
            else:
                data_list = []
                for _ in range(n):
                    data = int(input("Enter the data: "))
                    data_list.append(data)
                linked_list.Create_N_nodes(n, data_list)
        elif ch == 1:
            data = int(input("Enter the data: "))
            linked_list.insert_at_start(data)
        elif ch == 2:
            data = int(input("Enter the data: "))
            linked_list.insert_at_end(data)
        elif ch == 3:
            linked_list.delete_first_node()
        elif ch == 4:
            linked_list.delete_last_node()
        elif ch == 5:
            data = int(input("Enter the data: "))
            pos = int(input("Enter the position: "))
            linked_list.insert_at_position(data, pos)
        elif ch == 6:
            pos = int(input("Enter the position: "))
            linked_list.delete_at_position(pos)
        elif ch == 7:
            linked_list.display()
        elif ch == 8:
            print("Length of CLL is", linked_list.length)
        elif ch == 9:
            linked_list.delete_entire_list()
        elif ch == 10:
            print("Dhanyavad ji !")
            print("Created by")
            print("Aakash Jha")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
