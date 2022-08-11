import sys
import re

input = sys.stdin.readline

# 정답을 넣어줄 리스트
answer = []
for i in range(1, 6):
    # 문자열 입력
    find = input().rstrip()
    # 입력 받은 문자열 중에 "FBI"가 포함 되어 있다면 "FBI"만 따로 리스트 형태로 주어진다.
    if re.compile("FBI").findall(find):
        answer.append(i)
if not answer:
    print("HE GOT AWAY!")
else:
    print(*answer)