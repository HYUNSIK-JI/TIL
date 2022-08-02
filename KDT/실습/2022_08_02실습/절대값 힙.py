import sys
import heapq

input = sys.stdin.readline

n = int(input())
answer = []

for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(answer,(abs(a),a))
    else:
        if answer:
            print(heapq.heappop(answer)[1])
        else:
            print(0)