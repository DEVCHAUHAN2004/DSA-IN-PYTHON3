# nums = [1,2,3,4,5,6,7,8]
# class node:
#   def reverse_linked_list(nums,self):
#     temp = self.head
#     stack = []

#     while temp is not None:
#       stack.append(temp.value)
#       temp  = temp.next

#     temp = self.head
#     while temp is not None:
#       x = stack.pop()
#       temp.value = x
#       temp = temp.next
#     return head  

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # 🔹 Reverse function
    def reverse_linked_list(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.value)
            temp = temp.next
        temp = self.head
        while temp:
            temp.value = stack.pop()
            temp = temp.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


# -------- Main --------
nums = [1, 2, 3, 4, 5, 6, 7, 8]
ll = LinkedList()
for n in nums:
    ll.append(n)

print("Original List:")
ll.print_list()

ll.reverse_linked_list()

print("Reversed List:")
ll.print_list()
