import sys

input = sys.stdin.readline
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a > 0 and b > 0:
        Q1 += 1
    elif a > 0 and b < 0:
        Q4 += 1
    elif a < 0 and b > 0:
        Q2 += 1
    elif a < 0 and b < 0:
        Q3 += 1
    else:
        AXIS += 1
print(f"{'Q1:'} {Q1}")
print(f"{'Q2:'} {Q2}")
print(f"{'Q3:'} {Q3}")
print(f"{'Q4:'} {Q4}")
print(f"{'AXIS:'} {AXIS}")