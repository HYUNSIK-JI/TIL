import sys

input = sys.stdin.readline

n = int(input())
constructor = []

for num in range(1, n):
    hap = num + sum(list(map(int, str(num))))
    if hap == n:
        constructor.append(num)
        break
if not constructor:
    print(0)
else:
    print(*constructor)