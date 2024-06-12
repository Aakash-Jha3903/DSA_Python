from platform import node
import time
from xml.dom.minidom import Element


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
            for _ in range(n):
                print(temp.data, end=" <-> ")
                temp = temp.next
            print("head(again)")
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
        time.sleep(2)
        self.display()

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # DLL is not exists 
            self.head = new_node
        else:
            temp = self.head
            for _ in range(self.length):  # 4 node = 4times ????
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            # new_node.next = None  # Smart Python
        self.length += 1
        print("Node inserted at end.")
        self.display()

    def create_n_nodes(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
        # self.length = self.length + len(data_list)
        print("Doubly Linked List created successfully!")
        self.display()

    def delete_first_node(self):
        if self.head:
            if self.head.next:    #(imp.) for only one node 
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
        else:
             print("List is empty, no node to delete.")