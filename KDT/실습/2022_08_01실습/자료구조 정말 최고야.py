import sys

input = sys.stdin.readline

m, n = map(int, input().split())
for _ in range(n):
    k = int(input())
    lst = list(map(int, input().split()))

    for i in range(k - 1):
        if lst[i] < lst[i + 1]:
            print("No")
            exit()
print("Yes")