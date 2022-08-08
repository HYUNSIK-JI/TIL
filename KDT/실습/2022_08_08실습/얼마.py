import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    # 차 가격
    car = int(input())
    for _ in range(int(input())):
        # 부품 의수 q 부품당 가격 p
        q, p = map(int, input().split())
        car += q * p
    #최종가
    print(car)