import sys

input = sys.stdin.readline

n = int(input())

game = [list(map(str, input().split())) for _ in range(n)]
# 열 끼리 비교를 위해 zip함수 사용
game = list(map(list, zip(*game)))

# 점수 저장 리스트
scores = [0] * n

for score in game:
    for i in range(len(score)):
        # 같은 점수가 있는지 없는지 확인
        k = score.count(score[i])
        # 같은 점수가 있다면 2이상 일것.
        if k >= 2:
            # 0점 추가
            scores[i] += 0
        # 같은 점수가 없고 나만의 점수라면
        elif k == 1:
            # 그대로 합산
            scores[i] += int(score[i])
# 출력
print(*scores, sep="\n")