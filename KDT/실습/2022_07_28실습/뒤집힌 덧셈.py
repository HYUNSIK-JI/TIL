def reverse_num(n):
    return n[::-1]

a, b = map(str, input().split())
print(int(reverse_num(str(int(reverse_num(a)) + int(reverse_num(b))))))