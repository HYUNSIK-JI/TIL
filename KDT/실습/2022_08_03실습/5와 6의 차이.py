import sys

input = sys.stdin.readline

def smallsum(a, b):
    return int(str(a).replace('6', '5')) + int(str(b).replace('6', '5'))

def bigsum(a, b):
    return int(str(a).replace('5', '6')) + int(str(b).replace('5', '6'))

a, b = map(int, input().split())

print(smallsum(a, b), bigsum(a, b))