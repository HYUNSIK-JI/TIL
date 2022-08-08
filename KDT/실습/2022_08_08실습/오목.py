import sys

input = sys.stdin.readline

# 세로, 가로, 오른쪽 아래 대각선, 오른쪽 위 대각선
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

def check():
    # 오목판이 19 * 19 이므로다 돈다.
    for x in range(19):
        for y in range(19):
            # 만약 그곳이 흰돌 or 검은돌 이면
            if maps[x][y]:
                # 위에 언급한 4방향 탐색 진행
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 돌 카운트
                    cnt = 1
                    # 만약 범위를 벗어 나면 continue
                    if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
                        continue
                    # 만약 범위를 벗어 나지 않고 4방향 탐색을 진행 하기전 돌 과 4방향 탐색 했던 돌이 같은 색이면 while
                    while 0 <= nx < 19 and 0 <= ny < 19 and maps[x][y] == maps[nx][ny]:
                        # 같은 색 이므로 cnt += 1
                        cnt += 1
                        # 만약 5개 이상이면
                        if cnt == 5:
                            # 육목 nx, ny 과 nx + dx  ny + dy 색이 동일하면 육목
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and maps[nx][ny] == maps[nx+dx[i]][ny+dy[i]]:
                                break
                            # x - dx[i] 값과 y - dy[i] 값이 범위를 벗어나지 않고 x,y의 색와 x - dx, y- dy 색이 동일하면 육목
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and maps[x][y] == maps[x - dx[i]][y - dy[i]]:
                                break
                            # 두개다 아니면
                            # 오목.
                            return maps[x][y], x + 1, y + 1
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1
maps = [list(map(int, input().split())) for _ in range(19)]

color, x, y = check()
if not color:
    print(color)
else:
    print(color)
    print(x, y)