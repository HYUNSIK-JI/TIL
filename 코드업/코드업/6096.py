from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check(a,b):
    queue=deque()
    queue.append((a,b))

    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            while 0<=nx<19 and 0<=ny<19:
                if maps[nx][ny]==1:
                    maps[nx][ny]=0
                else:
                    maps[nx][ny]=1
                nx+=dx[i]
                ny+=dy[i]

maps=[]
for _ in range(19):
    w=list(map(int,input().split()))
    maps.append(w)
n=int(input())

for _ in range(n):
    x,y=map(int,input().split())
    check(x-1,y-1)
for i in range(19):
    print(*maps[i])