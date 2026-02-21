# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
# ---- Node Definition ----
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# ---- Remove Duplicates Function ----
def remove_duplicates(head):
    current = head
    
    while current is not None and current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
            
    return head


# ---- Print Linked List ----
def print_list(head):
    while head:
        print(head.value, end=" ")
        head = head.next
    print()


# ---- Create Linked List ----
# 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)


# ---- Call Functions ----
print_list(remove_duplicates(head))