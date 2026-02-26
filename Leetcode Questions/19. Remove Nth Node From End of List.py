class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# ---- Linked List Banana ----
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

n = 2    

# ---- Remove Nth Node from End ----
def remove_nth_node(head, n):
    slow = head
    fast = head

    for _ in range(n):
        fast = fast.next

    if fast is None:  # agar first node delete karni ho
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head

# ---- Print Linked List ----
def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()

# ---- Call Functions ----
print_list(remove_nth_node(head, n))