number=[0]*24
n=int(input())

a=list(map(int,input().split()))

for i in a:
    number[i]+=1
number.pop(0)
for i in number:
    print(i,end=" ")