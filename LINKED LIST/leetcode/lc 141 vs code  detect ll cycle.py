from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Function to check cycle
def hasCycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

# Creating the linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

# Test the function
print(hasCycle(head))  # Output: False
