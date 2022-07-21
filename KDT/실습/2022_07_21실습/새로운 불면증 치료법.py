#한꺼번에 출력하기 위한 리스트선언
p=[]
for test_case in range(1, int(input()) + 1):
    #0~9까지 번호를 봤는지를 체크 하기 위한 리스트 선언
    numbers = ["0", "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
    # 스타트 할 변수
    n = int(input())
    # 답을 넣기 위한 변수
    answer = 0
    # 0~9까지 번호를 다 봤는지 안봤는지 체크하기 위한 flag
    check = False
    #번호를 하나하나 넣을 리스트
    result = []
    #N*n을 위한 cnt 변수 선언
    cnt=1
    while True:
        k = str(n * cnt)
        for i in k:
            # result안에 중복이 있으면 넣지 않기 위한 조건문
            if i not in result:
                result.append(i)

                # 1~9번 다봤는지 확인
                if numbers == sorted(result):
                    # 다봣으면 해당 N*cnt값인 answer에 넣기
                    answer = int(k)
                    #while문을 탈출하기 위한 flag=True
                    check=True
                    break
        #0~9번 다 봤어요
        if check:
            #그럼 while문 나가자
            break
        #0~9번 다 못봤어요
        else:
            #그럼 숫자를 늘려보자
            cnt += 1
    #한꺼번에 출력하기 위한 p리스트에 추가
    p.append(f"#{test_case} {answer}")
#출력
for ans in p:
    print(ans)