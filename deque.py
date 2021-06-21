
# deque is double ended queue
# can add/remove elements form both ends

from collections import deque

d = deque()

# regular append to queue
d.append(1)
d.append(2)
d.append(3)

# append at beginning of queue
d.appendleft(4)

# remove from end of queue
#d.pop()

# remove from beginning of queue
#d.popleft()

# remove all elements
#d.clear()

# extend the list
d.extend([5,6,7])

# left extend the list
d.extendleft([8,9,10])
print(d)

d.rotate(-1)
print(d)