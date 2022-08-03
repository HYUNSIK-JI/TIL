import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(n)]

# 행,열 로 카운트 하기 위한 변수
row, col = 0, 0
for i in range(n):
    # 경비원이 없다면
    if not maps[i].count("X"):
        # 카운트
        row += 1

# 기존 maps의 행 을 열로 만든 2차원 리스트 형태로 변환
maps = list(map(list, zip(*maps)))

for i in range(n):
    # 경비원이 없다면
    if not maps[i].count("X"):
        # 카운트
        col += 1
print(col if row < col else row)