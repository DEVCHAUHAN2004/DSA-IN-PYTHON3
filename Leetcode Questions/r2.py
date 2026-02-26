class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    curr = head
    prev = None

    while curr is not None:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front

    return prev  # new head of the reversed list

# Example usage:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

# Reverse the linked list
x = reverse_linked_list(head)

# Print reversed list
temp = x
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")

