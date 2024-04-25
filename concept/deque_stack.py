from collections import deque

queue=deque()
#enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
#dequeue() O(1)
queue.popleft()
queue.popleft()
queue.popleft()


stack=[]
#push O(1)
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
#pop O(1)
stack.pop()
stack.pop()
stack.pop()