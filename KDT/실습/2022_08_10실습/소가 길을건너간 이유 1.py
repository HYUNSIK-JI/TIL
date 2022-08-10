cows = [[] for _ in range(11)]
answer = 0
for _ in range(int(input())):
    num, dir = map(int, input().split())
    if cows[num]:
        if cows[num][-1] != dir:
            cows[num].append(dir)
            answer += 1
        else:
            cows[num].append(dir)
    else:
        cows[num].append(dir)
print(answer)