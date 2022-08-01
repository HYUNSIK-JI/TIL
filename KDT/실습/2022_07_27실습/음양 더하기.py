def solution(absolutes, signs):
    answer = 0 # 합을 나타내기 위한 변수

    # 길이는 동일하다.
    for i in range(len(signs)):
        # signs[i]가 True 면
        if signs[i]:
            # 양수로 더하기
            answer += absolutes[i]
        # 반대라면
        else:
            # 음수로 더하기
            answer -= absolutes[i]

    return answer