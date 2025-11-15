class Box:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to next box


# Create 3 boxes: A → B → C
A = Box("A")
B = Box("B")
C = Box("C")

A.next = B
B.next = C

# Let's try printing one step and two steps
print("A.next:",  A.next.data)           # B
print("A.next.next:", A.next.next.data) # C

print("B.next:", B.next.data)           # C
print("B.next.next:", B.next.next)    # None (because C.next = None)"""
