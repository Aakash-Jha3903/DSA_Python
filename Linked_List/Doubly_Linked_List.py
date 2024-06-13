import time


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.length = 0

    def display(self):
        if self.head:
            print("This is your Doubly Linked List:")
            n = self.length
            temp = self.head
            print("None", end=" <-> ")
            for _ in range(n):
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("None")
        else:
            print("Linked list is empty!")

    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:  # DLL is not created
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        print("Node inserted at start.")
        self.display()

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # DLL is not exists
            self.head = new_node
            self.head.next = None
            self.head.prev = None
        else:
            temp = self.head
            while temp.next:
                # for _ in range(self.length):  # 4 node = 4times ????
                temp = temp.next
            temp.next = new_node  # AttributeError: 'NoneType' object has no attribute 'next'
            new_node.prev = temp
            # new_node.next = None  # Smart Python
        self.length += 1
        print("Node inserted at end.")
        self.display()

    def create_n_nodes(self, data_list):
        if self.head:
            print("Doubly Linked List already exists!")
            time.sleep(2)
            self.display()
            return

        for data in data_list:
            # self.insert_at_end(data)   # (May be not always work !)
            new_node = Node(data)
            if self.head is None:  # first node creation, always initially true
                # self.insert_at_start(data)
                self.head = new_node
                self.head.next = None
                self.head.prev = None
                temp = self.head
            else:
                # self.insert_at_end(data)
                temp.next = new_node
                new_node.prev = temp
                temp = temp.next  # OR temp = new_node ,order matters
                new_node.next = None
        self.length = self.length + len(data_list)
        print("Doubly Linked List created successfully!")
        self.display()

    def delete_first_node(self):
        if self.head:
            if self.head.next:  # (imp.) for only one node
                self.head = self.head.next  # i.e, None ,  self.head = None
                self.head.prev = None
            else:   # multiple nodes exists
                self.head = self.head.next
            self.length -= 1
            print("First node deleted.")
            self.display()
        else:
            print("List is empty, no node to delete.")

    def delete_last_node(self):
        if self.head:
            if self.length == 1:  # (imp.) Check if it's the only node
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
            self.length -= 1
            print("last node is deleted ")
            self.display()
        else:
            print("List is empty, no node to delete.")

    def insert_at_position(self, data, pos):
        if pos < 1 or pos > self.length + 1:
            print("Index out of range!")
            return
        new_node = Node(data)
        if pos == 1:
            # self.insert_at_start(data)   #(only this line (if pos ==1))Smart & precise
            if not self.head:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.head.prev = new_node
        else:
            temp = self.head
            for _ in range(pos - 2):   # Traverse to the node "before" the insertion point
                temp = temp.next
            new_node.next = temp.next
            temp.next.prev = new_node
            new_node.prev = temp
            temp.next = new_node
        self.length += 1
        print(f"Node inserted at position {pos}.")
        self.display()

    def delete_at_position(self, pos):
        if pos < 1 or pos > self.length:
            print("index out of range")
            return
        if pos == 1:
            # self.delete_first_node()   #(only this line (if pos ==1))Smart & precise
            if self.head.next:  # checks if the CLL has only one Node !
                self.head = self.head.next
                self.head.prev = None
        else:
            temp = self.head
            for _ in range(pos-2):  # Traverse to the node "before" the deletion point
                temp = temp.next
            temp.next.next.prev = temp
            temp.next = temp.next.next
        self.length -= 1
        print(f"Node at position {pos} deleted.")
        self.display()

    def delete_entire_list(self):
        self.head = None
        self.length = 0
        print("Entire list deleted.")
        self.display()


def menu():
    linked_list = DoublyLinkedList()
    while True:
        print("\n0. Create a Doubly Linked List with N nodes")
        print("1. Insert at start")
        print("2. Insert at end")
        print("3. Delete first node")
        print("4. Delete last node")
        print("5. Insert at position")
        print("6. Delete at position")
        print("7. Display Linked List")
        print("8. Display Length of DLL")
        print("9. Delete Entire List")
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
            else:
                data_list = []
                for _ in range(n):
                    data = int(input("Enter the data: "))
                    data_list.append(data)
                linked_list.create_n_nodes(data_list)
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
            print("This is your Doubly Linked List:")
            linked_list.display()
        elif ch == 8:
            print("Length of DLL is", linked_list.length)
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
