for test_case in range(1, int(input()) + 1):
    #두개의 시계 시,분 입력
    h_1, m_1, h_2, m_2 = map(int, input().split())

    #합
    h_hap = h_1+h_2
    m_hap = m_1+m_2

    # 60분이상 아니여도 나누기 60 진행
    h_hap += m_hap // 60

    # 60분이상 이면 +1 아니면 +0
    m_hap %= 60

    #출력
    print(f"#{test_case} {h_hap - 12} {m_hap}") if h_hap == 24 else print(f"#{test_case} {h_hap % 12} {m_hap}")
