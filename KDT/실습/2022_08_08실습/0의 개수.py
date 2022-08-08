import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    # 범위 설정 n ~ m
    n, m = map(int, input().rstrip().split())

    # 0의 갯수를 넣을 변수
    answer = 0
    for i in range(n, m + 1):
        # str(i)으로 변환하여 count 함수를 이용해 0의 갯수 계산
        answer += str(i).count("0")
    print(answer)