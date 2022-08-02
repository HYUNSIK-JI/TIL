# 풀이방법 : 재귀 이분 탐색 PyPy3 = 3092 ms 제출 // Python 3 제출시 재귀 인한 시간 초과 발생
import sys

input = sys.stdin.readline

def binary_search(start, end, target):
    if start > end:
        return 0
    mid = (start + end) // 2

    if note1[mid] == target:
        return 1
    elif note1[mid] < target:
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid - 1, target)

for test_case in range(int(input())):
    n1 = int(input())
    note1 = sorted(list(map(int, input().split())))

    n2 = int(input())

    note2 = list(map(int, input().split()))

    for i in note2:
        print(binary_search(0, n1 - 1, i))

# 풀이 방법: 재귀 X 이분 탐색 Python3 통과 코드 재귀 X PyPy3 = 2012 ms Python3 = 7012 ms
import sys

input = sys.stdin.readline

def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if note1[mid] == target:
            return 1
        elif note1[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0
for test_case in range(int(input())):
    n1 = int(input())
    note1 = sorted(list(map(int, input().split())))

    n2 = int(input())

    note2 = list(map(int, input().split()))

    for i in note2:
        print(binary_search(0, n1 - 1, i))

# 풀이법 딕셔너리 PyPy3 = 1528 ms Python3 = 1748 ms

import sys

input = sys.stdin.readline

for test_case in range(int(input())):

    n1 = int(input())
    note1= list(map(int, input().split()))

    n2 = int(input())
    note2 = list(map(int, input().split()))

    dictionary = {}

    for i in note1:
        dictionary[i] = dictionary.get(i, 0) + 1

    for i in note2:
        if i in dictionary:
            print(1)
        else:
            print(0)