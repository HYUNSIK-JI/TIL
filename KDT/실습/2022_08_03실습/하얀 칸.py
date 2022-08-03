# 풀이법1 하얀 칸
# chess = [list(input()) for _ in range(8)]
#
# cnt = 0
# for x in range(8):
#     for y in range(8):
#         if (x + y) % 2 == 0 and chess[x][y] == 'F':
#             cnt += 1
# print(cnt)

# 풀이법 2 BFS
import sys
from collections import deque

input = sys.stdin.readline

# 8방향 탐색
dx = [0, 0, 1, 1, 1, -1, 1, -1]
dy = [1, 1, 0, 0, 1, -1, -1, 1]

def bfs(a, b):
    # 문제 조건에 에 해당되는 위치가 있으면 카운트 하기 위한 변수
    cnt = 0
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위에 벗어나지 않고 방문하지 않았던 위치라면
            if 0 <= nx < 8 and 0 <= ny < 8 and not visit[nx][ny]:
                # 그곳이 말이 있는곳 이고 화이트 라면
                if maps[nx][ny] == "F" and colors[nx][ny] == "W":
                    #카운트
                    cnt += 1
                # 들렸던곳은 방문처리
                visit[nx][ny] = True
                # 큐에 넣기
                queue.append((nx, ny))
    return cnt
maps = [list(input().rstrip()) for _ in range(8)]
colors = [["W"] * 8 for _ in range(8)]

visit = [[False] * 8 for _ in range(8)]

# W,B 구분
for i in range(8):
    for j in range(8):
        if i == 0 and j % 2 != 0:
            colors[i][j] = "B"
        elif i % 2 != 0 and j % 2 == 0:
            colors[i][j] = "B"
        elif i % 2 == 0 and j % 2 != 0:
            colors[i][j] = "B"
print(bfs(0, 0))