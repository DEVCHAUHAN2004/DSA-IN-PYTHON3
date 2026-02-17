class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_at(self, position):

        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if position == 0:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        count = 0

        while curr is not None and count < position:
            prev = curr
            curr = curr.next
            count += 1

        if curr is None:
            print("Position out of range")
            return

        prev.next = curr.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")


# Example
ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
# ll.head.next.next.ne
