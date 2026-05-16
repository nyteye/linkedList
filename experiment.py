class Node:
    def __init__(self, data):
        self.data = data  # Stores the actual value
        self.next = None


#n1-n2-n3-NONE

n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n1.next = n2
n2.next = n3

print(id(n1.next))
print(id(n1.next))
print(id(n2))

print(dir(n2))
