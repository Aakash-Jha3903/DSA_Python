class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

# display the data of linked list  
i = a
# while (i != None):   # parenthesis is not compulsary 
# while i != None:     # "!=" can be replace by "is not"
while i is not None:
    print(i.data)
    i = i.next


# print("The value of a is ")
# print(a.data)
# print("The address(next) of a is ")
# print(a.next)

# id of nodes....................................................
# print(id(a))
# print(id(b))
# print(id(c))

# difference between their ids ..................................................
# print(id(a) - id(b))
# print(id(b) - id(c))
# print(id(a) - id(c))
