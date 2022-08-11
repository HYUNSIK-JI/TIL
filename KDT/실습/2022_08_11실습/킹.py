import sys

input = sys.stdin.readline

# 포지션의 인덱스를 이용해 ord, chr를 위한 리스트
position = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 각 커맨드 당 8방향
commands = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T' : [-1, 0], 'RT' : [-1, 1], 'LT' : [-1, -1], 'RB' : [1, 1], 'LB': [1, -1]}

# 킹의 위치, 스톤의 위치, 명령의 개수
king, stone, n = input().rstrip().split()

# 위치 조작
kx, ky = 8 - int(king[1]), position[ord(king[0]) - 65]
sx, sy = 8 - int(stone[1]), position[ord(stone[0]) - 65]

maps = [[0] * 8 for _ in range(8)]

for _ in range(int(n)):
    command = input().rstrip()
    dx, dy = commands[command]

    nx = kx + dx
    ny = ky + dy
    # 킹 와 스톤의 위치가 범위 내에 있는지 파악
    if 0 <= nx < 8 and 0 <= ny < 8 and 0 <= sx < 8 and 0 <= sy < 8:
        # 만약 킹이 움직일려고 하는 위치가 스톤의 위치라면
        if nx == sx and ny == sy:
            # 만약 스톤의 위치에서 델타 값 을 더한 위치가 범위내 있는지 파악
            if 0 <= sx + dx < 8 and 0 <= sy + dy < 8:
                sx, sy = sx + dx, sy + dy
                kx, ky = nx, ny
            # 범위가 벗어나면 다음 명령어
            else:
                continue
        else:
            kx, ky = nx, ny

result1, result2 = "", ""

result1 += chr(position[ky] + 65) + str(8 - kx)
result2 += chr(position[sy] + 65) + str(8 - sx)

print(result1)
print(result2)