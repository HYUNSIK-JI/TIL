A, B, C = map(int, input().split())

prices = [list(map(int, input().split())) for _ in range(3)]

mx = max(prices[0][1], prices[1][1], prices[2][1])

answer = [0] * (mx - 1)

for time in prices:
    for i in range(time[0] - 1, time[1] - 1):
        answer[i] += 1

result = 0

for num in answer:
    if num == 1:
        result += A
    elif num == 2:
        result += 2 * B
    elif num == 3:
        result += 3 * C
print(result)