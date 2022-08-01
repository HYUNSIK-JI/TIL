import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    stack = []
    check = False
    galho = input().rstrip()

    for i in galho:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                check = True
                break
    if check:
        print("NO")
    else:
        if stack:
            print("NO")
        else:
            print("YES")