import sys

sys.stdin = open("3_OX퀴즈.txt")

input = sys.stdin.readline

for test_case in range(int(input())):
    stack = []
    answer = 0
    OX = input().rstrip()

    for i in OX:
        if i == "O":
            stack.append(i)
            answer += len(stack)
        else:
            stack = []
    print(answer)