import sys

input = sys.stdin.readline

kakao_2017 = [0, 5000000, 3000000, 2000000, 500000, 300000, 100000]
kakao_2018 = [5120000, 2560000, 1280000, 640000, 320000]

for _ in range(int(input())):
    hap = 0
    a, b = map(int, input().split())
    if a + b == 0:
        print(hap)
    else:
        # 2017년도 본선은 1~21등 사람 만 상금을 탈수 있으므로
        if 1 <= a <= 21:
            # 각 등수 마다 매겨진 상금 및 인원 체크를 위한 반복문
            for i in range(1, 7):
                a -= i
                if a <= 0:
                    hap += kakao_2017[i]
                    break
        # 2018년도 본선은 1~31등 사람 만 상금을 탈수 있으므로
        if 1 <= b <= 31:
            # 각 등수 마다 매겨진 상금 및 인원 체크를 위한 반복문
            for i in range(6):
                if (2 ** i) <= b < 2 ** (i + 1):
                    hap += kakao_2018[i]
                    break
        print(hap)