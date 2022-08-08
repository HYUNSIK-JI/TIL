import sys

input = sys.stdin.readline

# 난쟁이들 입력 받고 정렬
seven = sorted([int(input()) for _ in range(9)])

# 난쟁이들 키 의 합
hap = sum(seven)
check = False

for i in range(9):
    for j in range(i + 1, 9):
        a = seven[i]
        b = seven[j]
        # 만약 9명중 2명을 뺀 키의 합이 100이면 break
        if hap - (a + b) == 100:
            check = True
            break
    if check:
        break
#오름 차순을 출력을 위함
seven.sort()
for i in seven:
    # a 와 b가 아니면 출력
    if i != a and i != b:
        print(i)