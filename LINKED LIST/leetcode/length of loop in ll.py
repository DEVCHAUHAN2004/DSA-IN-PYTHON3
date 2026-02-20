class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def length_of_loop(head):   # ❌ removed self
    temp = head
    visited = {}
    index = 0

    while temp is not None:
        if temp in visited:
            return index - visited[temp]
        visited[temp] = index
        index += 1
        temp = temp.next

    return 0


# -------- Bigger Linked List --------

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n4   # Loop starts from node 4

print("Loop length is:", length_of_loop(head))