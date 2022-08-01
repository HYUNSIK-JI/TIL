import sys
from math import gcd

input = sys.stdin.readline

n, m = map(int, input().split())
number_gcd = gcd(n, m)

print(number_gcd)
print(n * m // number_gcd)

# 2번째 유클리드 호제법

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())
print(gcd(n, m))
print(lcm(n, m))