import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

answer = []

# 중복 되지 않고 3 장의 카드를 뽑기 위함 3중 반복문
for x in range(1, n):
    for y in range(x + 1, n):
        for z in range(y + 1, n):
            # 카드의 합이 m를 넘지 않는것 중 최대를 원함
            hap = cards[x] + cards[y] + cards[z]
            if hap <= m:
                # answer 합류
                answer.append(hap)
# 그중 가장 큰값
print(max(answer))