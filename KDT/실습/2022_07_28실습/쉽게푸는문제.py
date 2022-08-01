a,b = map(int, input().split())
n = []
for i in range(1, 1001):
    for j in range(i):
        n.append(i)
print(sum(n[a - 1:b]))