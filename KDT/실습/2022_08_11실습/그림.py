import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                if not visit[nx][ny]:
                    visit[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
    return cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

answer = []

for i in range(n):
    for j in range(m):
        if not visit[i][j] and graph[i][j]:
            answer.append(BFS(i, j))
if answer:
    print(len(answer), max(answer), sep="\n")
else:
    print(0, 0, sep="\n")