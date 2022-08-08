# 정규 표현식을 연습하기 위해 정규 표현식을 사용하였음
import re
# 몇번째 영화 인지 입력
n = int(input())
cnt = 0
start = 666
while True:
    # '666' 을 매치로 하여 start중 '666' 포함하고 있는지 없는지 확인 하기 위한 조건문
    if re.compile('666').findall(str(start)):
        cnt += 1
        if cnt == n:
            # 찾고 있던 n의 번째 영화이면 start를 출력
            print(start)
            break
    start += 1