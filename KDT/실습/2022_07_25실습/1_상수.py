import sys

# sys.stdin = open("1_상수.txt")
input = sys.stdin.readline

A, B = map(str, input().rstrip().split())

for i in range(3):
    if int(A[-i - 1]) < int(B[-i - 1]):
        print(B[::-1])
        break
    elif int(A[-i - 1]) > int(B[-i - 1]):
        print(A[::-1])
        break