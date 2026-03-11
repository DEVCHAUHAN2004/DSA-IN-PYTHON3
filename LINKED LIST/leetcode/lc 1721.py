# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k):
        first = head
        
        for i in range(k-1):
            first = first.next
        
        a = first
        second = head
        
        while first.next:
            first = first.next
            second = second.next
        
        a.val, second.val = second.val, a.val
        
        return head


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

obj = Solution()
new_head = obj.swapNodes(head, k)

# Print linked list
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next