import sys

input = sys.stdin.readline
bracket = ["(", ")", "[", "]"]
while True:
    stack = []
    sentence = input().rstrip()
    check = False
    if sentence[0] == ".":
        break
    for i in sentence:
        if i in bracket:
            if i == "(" or i == "[":
                stack.append(i)
            else:
                if stack:
                    if i == ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            print("no")
                            check = True
                            break
                    else:
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            print("no")
                            check = True
                            break
                else:
                    print("no")
                    check = True
                    break
    if not check:
        if stack:
            print("no")
        else:
            print("yes")