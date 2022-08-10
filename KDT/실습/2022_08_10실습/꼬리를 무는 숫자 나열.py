a, b = map(int, input().split())
# 4로 나누어지면 좌표 표시가 안되므로 각각 -1
a, b = a - 1, b - 1
print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))