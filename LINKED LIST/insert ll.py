class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Node:
    def __init__(self):
        self.head = None

    def insert_at(self, value, position):
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        prev_node = None
        count = 0

        while curr is not None and count < position:
            prev_node = curr
            curr = curr.next
            count += 1

        if prev_node is not None:
            prev_node.next = new_node
            new_node.next = curr

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")


# ---- Example ----

ll = Node()

ll.insert_at(10, 0)
ll.insert_at(20, 1)
ll.insert_at(30, 2)
ll.insert_at(25, 2)

ll.print_list()
