import sys

input = sys.stdin.readline

# S =  (R1 + R2) // 2의 평균 값이다.
# 2S = R1 + R2
# R2 = 2S - R1

R1, S = map(int, input().split())
print((S * 2) - R1)