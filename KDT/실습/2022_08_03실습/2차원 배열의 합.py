import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 입력 값의 혼동을 줄이기 위해 앞에 m개의 수만큼 2차원 리스트 형태로 추가  ex) m = 3 [[0, 0, 0]]
maps = [[0] * m] + [list(map(int, input().split())) for _ in range(n)]

for _ in range(int(input())):
    hap = 0
    x1, y1, x2, y2 = map(int, input().split())
    # for문은 x2 - 1 까지만 작동 하므로 x2 + 1으로!
    for i in range(x1, x2 + 1):
        # y1 같은경우 1이 더 많으므로 -1
        for j in range(y1 - 1, y2):
            if x1 - 1 <= i <= x2 and y1 - 1 <= j <= y2:
                hap += maps[i][j]
    print(hap)