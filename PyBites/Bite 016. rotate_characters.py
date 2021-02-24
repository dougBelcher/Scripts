# 16. Rotate characters in string
# https://docs.python.org/3.9/library/collections.html#collections.deque.rotate
from collections import deque

s = "PyBites hits 250 tips"
d = deque(s)
n = 7
d.rotate(n)
print(f"{d}")
''.join(d)
print(f"{d}")
d = deque(s)
d.rotate(-n)
''.join(d)
print(f"{d}")
