import sys

input = sys.stdin.readline

A = []

for i in range(int(input())):
    A.append(int(input()))

for i in sorted(A):
    print(i)