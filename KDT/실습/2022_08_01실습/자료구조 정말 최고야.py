import sys

input = sys.stdin.readline

# 이 문제의 핵심 오름차순으로 놓을수 있으냐 없느냐
# 스택이 아닌 단순 비교로도 풀수 있는 문제이다.
# 내림 차순으로 놓여야 있어야 오름차순으로 정렬이 가능한것이다. 핵심!!
m, n = map(int, input().split())
for _ in range(n):
    k = int(input())
    book = list(map(int, input().split()))

    for i in range(k - 1):
        if book[i] < book[i + 1]:
            print("No")
            exit()
print("Yes")