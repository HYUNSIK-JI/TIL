import sys
from collections import deque

input = sys.stdin.readline
# 8방향
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [0, -1, 1, 1, 1, 0, -1, -1]

def BFS(a, b):
    # 방문 처리
    visit[a][b] = True
    # queue에 넣기
    queue = deque()
    queue.append((a, b))

    while queue:
        # x, y 로 빼기
        x, y = queue.popleft()
        # 8방향 탐색 시작
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어 나지 않고 방문하지 않았던 곳 이고 그곳이 땅 이라면
            if 0 <= nx < h and 0 <= ny < w and not visit[nx][ny] and maps[nx][ny] == 1:
                # 방문 처리 후
                visit[nx][ny] = True
                # 큐에 넣기
                queue.append((nx, ny))

while True:
    # 넓이, 높이 입력
    w, h = map(int, input().split())
    # 만약 w, h  둘다 0이면 while 문 종료
    if w == 0 and h == 0:
        break
    # 지도 정보 입력
    maps = [list(map(int, input().split())) for _ in range(h)]
    # 방문 요소 체크
    visit = [[False] * w for _ in range(h)]
    # 섬의 개수
    land_cnt = 0
    for i in range(h):
        for j in range(w):
            # maps[i][j] 가 육지 이고 방문하지 않았던 곳 인지 파악
            if maps[i][j] == 1 and not visit[i][j]:
                # 위에 조건이 성립이 되면 BFS()함수 실행
                BFS(i, j)
                # BFS안에서 연결 된 육지들은 섬이다.
                land_cnt += 1
    print(land_cnt)