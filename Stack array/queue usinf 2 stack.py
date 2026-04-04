class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())

        # Insert new element
        self.s1.append(x)

        # Move back to s1
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue is empty")
            return
        return self.s1.pop()

    def front(self):
        if len(self.s1) == 0:
            print("Queue is empty")
            return
        return self.s1[-1]

    def is_empty(self):
        return len(self.s1) == 0

    def size(self):
        return len(self.s1)


# 🔹 Main Program (VS Code run)
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue size:", q.size())
print("Front element:", q.front())

print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())

print("Front element:", q.front())
print("Is empty:", q.is_empty())