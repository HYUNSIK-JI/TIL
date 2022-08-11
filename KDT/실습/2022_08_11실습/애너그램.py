import sys

input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(str, input().split())

    a = sorted(A)
    b = sorted(B)

    if a == b:
        print(f"{A} {'&'} {B} {'are'} {'anagrams.'}")
    else:
        print(f"{A} {'&'} {B} {'are'} {'NOT'} {'anagrams.'}")