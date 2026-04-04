class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.pop()

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)

print("stack content =", stack.items)   # 👈 fix

print("pop item =", stack.pop())

print("stack content =", stack.items)   # 👈 fix

print("top item after pop =", stack.top())  # 👈 fix

print("stack is empty =", stack.is_empty())