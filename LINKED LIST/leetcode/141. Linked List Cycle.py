# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
        return False        
        


# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class Solution(object):
#     def hasCycle(self, head):
#         temp = head
#         my_set = set()

#         while temp is not None:
#             if temp in my_set:
#                 return True
#             my_set.add(temp)
#             temp = temp.next
#         return False


# # --------- Create Linked List ---------
# # 1 -> 2 -> 3 -> 4 -> 5
# head = ListNode(1)
# second = ListNode(2)
# third = ListNode(3)
# fourth = ListNode(4)
# fifth = ListNode(5)

# head.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth

# # 🔁 Create Cycle (5 -> 3)
# fifth.next = third   # comment this line to remove cycle


# # --------- Run Solution ---------
# sol = Solution()
# print(sol.hasCycle(head))
