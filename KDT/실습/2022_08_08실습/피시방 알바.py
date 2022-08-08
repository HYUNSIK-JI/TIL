import sys

input = sys.stdin.readline

# 손님 수
n = int(input())

# 같은 자리에 있을땐 앉지 못하는 손님 발생
# 중복 제거를 위한 set 설정

lst = set(list(map(int, input().split())))
# 총 손님수 - 중복 제거 한 손님의수면
# 중복 된 자리때문에 앉지 못한 손님의 수!
print(n - len(lst))