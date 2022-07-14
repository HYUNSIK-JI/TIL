h,w=map(int,input().split())
maps=[[0]*w for _ in range(h)]

n=int(input())

for _ in range(n):
    l,d,a,b=map(int,input().split())
    a,b=a-1,b-1
    maps[a][b]=1
    l-=1
    while l>0:
        if d==0:
            b+=1
            maps[a][b]=1
            l-=1
        else:
            a+=1
            maps[a][b]=1
            l-=1
for i in range(h):
    print(*maps[i])