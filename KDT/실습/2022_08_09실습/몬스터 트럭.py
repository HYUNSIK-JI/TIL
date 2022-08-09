import sys

input = sys.stdin.readline

def check(lst):
    space = 0
    car = 0
    for i in lst:
        for j in i:
            if j == ".":
                space += 1
            elif j == "X":
                car += 1
            else:
                return 0, 0
    return space, car
r, c = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(r)]
answer = [0] * 5
# 자동차의 크기는 2 * 2
for i in range(r - 2 + 1):
    for j in range(c - 2 + 1):
        # 맵 중에서 2 * 2 크기에서 자동차의 개수 와 빈 공간 갯수 파악
        k = check([maps[i + x][j:j + 2] for x in range(2)])
        # 빈 공간만 있으면 answer의 0번째 인덱스 + 1
        if k[0] == 4 and k[1] == 0:
            answer[0] += 1
        # 빈 공간이 3개 이며 자동차가 1개 주차되 있다면 answer의 1번째 인덱스 + 1
        elif k[0] == 3 and k[1] == 1:
            answer[1] += 1
        # 빈 공간이 2개 이며 자동차가 2개 주차되 있다면 answer의 2번째 인덱스 + 1
        elif k[0] == 2 and k[1] == 2:
            answer[2] += 1
        # 빈 공간이 1개 이며 자동차가 3개 주차되 있다면 answer의 3번째 인덱스 + 1
        elif k[0] == 1 and k[1] == 3:
            answer[3] += 1
        # 빈 공간이 0개 이며 자동차가 4개 주차되 있다면 answer의 4번째 인덱스 + 1
        elif k[0] == 0 and k[1] == 4:
            answer[4] += 1
print(*answer, sep="\n")