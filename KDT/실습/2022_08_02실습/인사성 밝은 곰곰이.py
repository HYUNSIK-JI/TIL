import sys

input = sys.stdin.readline

cnt = 0
for _ in range(int(input())):
    name = input().rstrip()
    if name == "ENTER":
        bear = set()
    else:
        if name not in bear:
            bear.add(name)
            cnt += 1
print(cnt)