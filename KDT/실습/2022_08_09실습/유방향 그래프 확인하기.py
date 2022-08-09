import sys
from pprint import pprint
input = sys.stdin.readline

n, m = map(int, input().split())
adj1 = [[0] * (n + 1) for _ in range(n + 1)]
adj2 = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj2[a].append(b)
    adj1[a][b] = 1
pprint(adj1)
print(adj2)