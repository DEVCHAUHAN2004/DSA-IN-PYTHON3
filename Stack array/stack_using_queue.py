from collections import deque

class stack_using_queue:

    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

        # rotate queue
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "stack is empty"
        return self.queue.popleft()

    def peek(self):
        if len(self.queue) == 0:
            return "stack is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# 🔹 Driver Code (VS Code run)
stack = stack_using_queue()

stack.push(5)
stack.push(10)
stack.push(15)

print("stack =", list(stack.queue))   # 👈 print actual content

print("pop =", stack.pop())

print("stack =", list(stack.queue))

print("peek =", stack.peek())

print("is empty =", stack.is_empty())

print("size =", stack.size())