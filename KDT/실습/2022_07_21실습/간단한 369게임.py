for i in range(1, int(input()) + 1):
    #각 숫자마다 3 , 6 , 9가 몇개씩 있는지 카운트
    cnt = str(i).count("3") + str(i).count("6") + str(i).count("9")

    #cnt == 0 이면 숫자 그대로 출력 아니면 cnt 갯수 만큼 -출력
    print(i, end=" ") if not cnt else print("-" * cnt, end=" ")
