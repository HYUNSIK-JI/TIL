import sys

input = sys.stdin.readline

# 방향 및 x, y 계산을 위함
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())
x, y = 0, 0
dir = 0
check = False

for _ in range(n):
    # 커맨드, 숫자
    com, num = map(str, input().rstrip().split())

    if com == "TURN":
        if num == "1":
            dir -= 1
            if dir < 0:
                dir = 3
        else:
            dir += 1
            if dir > 3:
                dir = 0
    elif com == "MOVE":
        x += int(num) * dx[dir]
        y += int(num) * dy[dir]
        if x < 0 or x >= m or y < 0 or y >= m:
            print(-1)
            check = True
            break
if not check:
    print(y, x)