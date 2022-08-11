import sys

input = sys.stdin.readline

for _ in range(3):
    num = input().rstrip()
    # 부분 문자열은 본인 혼자만 있을수 있기 때문에 무조건 1로 시작한다.
    length = 1
    mx = 0
    for i in range(len(num) - 1):
        # 만약 다음 문자가 동일한지 파악
        if num[i] == num[i + 1]:
            # 동일하면 + 1
            length += 1
        # 만약 다음 문자가 동일하지 않으면
        else:
            # 지금 까지 제일 길었던 length값 비교
            mx = max(mx, length)
            # 길이 값 초기화
            length = 1
    # 연속적으로 같은 숫자가 나올수도 있으므로 ex) 99999 이 경우를 대비해서 반복문이 끝난후 비교
    mx = max(mx, length)
    print(mx)