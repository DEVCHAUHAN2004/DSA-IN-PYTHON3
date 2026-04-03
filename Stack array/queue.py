class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)   # rear pe add

    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self.items.pop(0)  # front se remove

    def front(self):
        if self.is_empty():
            return "queue is empty"
        return self.items[0]

    def rear(self):
        if self.is_empty():
            return "queue is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)


# use
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("queue =", q.items)

print("front =", q.front())
print("rear =", q.rear())

print("dequeue =", q.dequeue())

print("queue =", q.items)

print("size =", q.size())

print("is empty =", q.is_empty())