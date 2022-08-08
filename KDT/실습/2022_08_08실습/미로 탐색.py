import sys
from collections import deque

# 4 뱡향 탐색 을 위한 델타 값
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    # 0, 0 를 큐에 넣고 진행
    queue.append((a, b))
    
    # 문제에서 시작점 과 끝점을 카운트 한다는 말이 있다.
    # 그러므로 첫번째 지점인 0, 0 도 1번 움직인 걸로 한다.
    visit[a][b] = 1

    while queue:
        # 최초 0, 0를 x ,y로 빼고 4방향 탐색진행
        # 두번째부터는 범위를 벗어 나지 않고 이동 할수 있는 길인 1 인 것들만 queue의 x,y로 들어옴
        x, y = queue.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 만약 범위를 벗어 나지 않으며
            if 0 <= nx < n and 0 <= ny < m:
                # 우리가 원하는 이동하는 길이며 방문하지 않았던 곳이라면
                if maps[nx][ny] == "1" and not visit[nx][ny]:
                    # 지나왔었던 곳의 움직인 횟수에서 + 1
                    visit[nx][ny] = visit[x][y] + 1
                    # 만약 그곳이 도착지 라면
                    if nx == n - 1 and ny == m - 1:
                        # 움직인 횟수를 리턴
                        return visit[nx][ny]
                    queue.append((nx, ny))

input = sys.stdin.readline

n, m = map(int, input().split())

# 미로!! 입력
maps = [list(input().rstrip()) for _ in range(n)]

# 최솟 값으로 움직이고 방문 했던 곳을 방문 표시 해주는 visit 리스트
visit = [[0] * m for _ in range(n)]

# 문제에서 도착하지 못하는 경우는 없다고 했으니 다른 출력이 필요없음
print(bfs(0, 0))