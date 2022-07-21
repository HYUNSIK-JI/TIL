for test_case in range(1, int(input()) + 1):
    #회문을 판별할 단어 입력
    word=input()

    #슬라이싱을 이용해 맨 뒤에서 맨 앞으로 -> word[::-1]
    print(f"#{test_case} {1}") if word==word[::-1] else print(f"#{test_case} {0}")