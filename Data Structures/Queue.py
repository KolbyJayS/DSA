from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.appendleft() # Appends left element in O(1)
queue.popleft() # Pops left element in O(1)
queue.append() # Appends right element in O(1)
queue.pop() # Pops right element in O(1)