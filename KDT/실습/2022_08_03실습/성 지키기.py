import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(n)]

# 기존의 maps의 n * m 상태를 - > m * n으로 변경
maps2 = list(map(list, zip(*maps)))

row, col = 0, 0
for i in range(n):
    if not maps[i].count("X"):
        row += 1
for i in range(m):
    if not maps2[i].count("X"):
        col += 1
print(max(row, col))
