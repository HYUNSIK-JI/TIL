import sys

input = sys.stdin.readline

find = ["a", "e", "i", "o", "u"]
while True:
    cnt = 0
    sentence = input().rstrip().lower()
    if sentence == "#":
        break
    for i in sentence:
        for j in i:
            if j in find:
                cnt += 1
    print(cnt)