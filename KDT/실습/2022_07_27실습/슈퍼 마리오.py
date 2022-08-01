#합을 넣어줄 변수
hap = 0

# 최솟값 비교 변수
mn = int(1e9)

# 답
answer = 0

for i in range(10):

    hap += int(input())
    # 100과 의 차이가 가장 적은 곳을 찾기 위한 조건문
    if abs(100 - hap) <= mn:
        mn = abs(100 - hap)
        # 차이가 똑같다면 값이 높은 숫자를 찾기위한 조건문
        if answer < hap:
            answer = hap
print(answer)