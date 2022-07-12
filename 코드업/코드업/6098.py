maps=[list(map(int,input().split())) for _ in range(10)]

x,y=1,1
maps[1][1]=9

while True:
    if maps[x][y+1]==0:
        y+=1
        maps[x][y] = 9

    elif maps[x][y+1]==1:
        if maps[x+1][y]==1:
            break
        elif maps[x+1][y]==2:
            x += 1
            maps[x][y]=9
            break
        else:
            x += 1
            maps[x][y]=9
    else:
        y += 1
        maps[x][y] = 9
        break

for i in range(10):
    print(*maps[i])