from collections import deque

n = int(input())
li = deque(enumerate(map(int, input().split())))
print(li)
li.rotate(-1)
print(li)
