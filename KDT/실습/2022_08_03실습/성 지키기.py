import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(n)]
maps2 = list(map(list, zip(*maps)))

row, col = 0, 0
for i in range(n):
    if not maps[i].count("X"):
        row += 1
for i in range(m):
    if not maps2[i].count("X"):
        col += 1
print(max(row, col))
