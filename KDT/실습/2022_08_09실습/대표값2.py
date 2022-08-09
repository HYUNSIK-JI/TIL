import sys

input = sys.stdin.readline

lst = sorted([int(input()) for _ in range(5)])
print(sum(lst) // 5)
print(lst[5 // 2])