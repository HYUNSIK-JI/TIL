for i in range(1, int(input()) + 1):
    i = str(i)
    #각 숫자마다 3 , 6 , 9가 몇개씩 있는지 카운트
    cnt = i.count("3") + i.count("6") + i.count("9")

    #cnt == 0 이면 숫자 그대로 출력 아니면 cnt 갯수 만큼 -출력
    print(i, end=" ") if cnt == 0 else print("-" * cnt, end=" ")