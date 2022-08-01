import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
answer = []
hap = 0
for i in range(1, n):

    if road[i - 1] < road[i]:
        hap += road[i] - road[i - 1]
    else:
        answer.append(hap)
        hap = 0
if hap:
    answer.append(hap)
if answer:
    print(max(answer))
else:
    print(0)