class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(8)
node4 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4

#   INSE ADDRESS PRINT HOGE
# print(node1)
# print(node2)
# print(node3)
# print(node4)

# print(node1.value)
# print(node2.value)
# print(node3.value)
# print(node4.value)
# 5
# 10
# 8
# 7

print(node1.value)
print(node1.next.value)    #node2 
print(node1.next.next.value)   #node 3
print(node1.next.next.next.value)   #node4

print(node2.next.value)  #8



