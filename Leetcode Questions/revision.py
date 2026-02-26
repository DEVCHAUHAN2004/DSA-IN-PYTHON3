# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# def middle_ll(head):
#     curr = head
#     count = 0
    
#     # Count the number of nodes
#     while curr:
#         curr = curr.next
#         count += 1

#     curr = head
#     # Move to the middle node
#     for i in range(count // 2):
#         curr = curr.next

#     return curr  # returns the middle node

# # Example linked list
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# mid_node = middle_ll(head)
# print("Middle node value:", mid_node.val)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def middle_ll(self):
        slow = self
        fast = self

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow  # returns the middle node

# Example linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Get middle node
mid_node = head.middle_ll()
print("Middle node value:", mid_node.val)

