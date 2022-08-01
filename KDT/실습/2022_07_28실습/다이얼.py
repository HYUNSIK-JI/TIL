dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
words = input()
answer = 0
for word in words:
    for alpha in dial:
        if word in alpha:
            answer += dial.index(alpha) + 3
print(answer)