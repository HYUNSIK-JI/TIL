# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# q = deque()
#
# for i in range(1,n+1):
# 	q.append(i)
#
# while q:
#     a = q.popleft()
#     print(a, end = " ")
#     if q:
#         q.append(q.popleft())

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()

for i in range(1, n + 1):
    q.append(i)

while q:
    a = q.popleft()
    print(a, end=" ")
    q.rotate((len(q) - 1))