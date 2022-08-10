a = int(input())
b = int(input())
c = int(input())

k = a + b + c
if k == 180 and a == 60 and b == 60:
    print("Equilateral")
elif k == 180 and a == b or a == c or b == c:
    print("Isosceles")
elif k == 180 and a != b != c:
    print("Scalene")
elif k != 180:
    print("Error")