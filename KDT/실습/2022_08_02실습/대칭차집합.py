# 풀이 방법 set 의 교집합, 합집합, 차집합 성질 이용
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a - b) + len(b - a))