from collections import deque

n = deque([])

n.append(10)
n.append(20)
n.append(30)

n.appendleft(5)
n.appendleft(8)

print(n)

n.popleft()
print(n)
n.clear()
print(n)
