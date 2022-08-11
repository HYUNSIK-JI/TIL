import sys

input = sys.stdin.readline

x = int(input())
price = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    price += a * b
if x == price:
    print("Yes")
else:
    print("No")