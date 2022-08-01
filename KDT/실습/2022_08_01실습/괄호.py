import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    stack = []
    check = False
    galho = input().rstrip()

    for i in galho:
        # "(" 은 무조건 넣어~
        if i == "(":
            stack.append(i)
        else:
            # 스택이 비어있지 않으면 안에있는건 무조건 "("!!
            if stack:
                # 그럼 꺼내요 올바른 괄호잖아요
                stack.pop()
            else:
                # 없으면.. 올바른 괄호가 아닌거예요
                check = True
                print("NO")
                break
    # 이미 출력 한적 없다면
    if not check:
        # 남아 있는게 있다면 올바른 괄호가 아니예요
        if stack:
            print("NO")
        else:
            print("YES")