n=int(input())

if n%3==0 and n%2==0 and n!=0:
    print("참")
else:
    print("거짓")

####################

word=input()
cnt=0

for i in word:
    cnt+=1
print(cnt)


#################

n=int(input())
answer=0

for i in range(1,n+1):
    answer+=i
print(answer)
#################

n=int(input())
answer=1

for i in range(1,n+1):
    answer*=i
print(answer)
#################

n_list=list(map(int,input()))
hap=0
cnt=0
for i in n_list:
    hap+=i
    cnt+=1
# 소수점 이하 까지표시
print(hap/cnt)
# 소수점 생략
print(hap//cnt)


n_list=list(map(int,input()))
mn=1e9

for i in n_list:
    if mn>i:
        mn=i
print(mn)

########

n_list=sorted(list(map(int,input().split())))
print(n_list[-2])


n_list=list(set(map(int,input().split())))
first_mx=-1e9
second_mx=-1e9

for i in n_list:
    if first_mx<i:
        first_mx=i
for i in n_list:
    if i!=first_mx:
        if second_mx<i:
            second_mx=i
print(second_mx)

import sys

input=sys.stdin.readline

# 14.문자의 갯수 구하기
word=input().strip()
count_a=0

for i in word:
    if i=="a":
        count_a+=1
print(i)

# 15.문자의 위치 구하기
word=input()

for i in range(len(word)):
    if word[i]=="a":
        print(i)
        check=True
        break
else:
    print(-1)

# 15-1.문자의 위치 구하기
word=input()

for i in range(len(word)):
    if word[i]=="a":
        print(i,end=" ")

# 16.모음 등장 여부 확인하기
word=input().rstrip()
alpha=["a","o","i","u","e"]

alpha_count=0

for i in word:
    if i in alpha:
        alpha_count+=1
print(alpha_count)

# 17.소문자-대문자 변환하기
word=input().rstrip()

for i in word:
    k=ord(i)
    if 65<=k<97:
        print(chr(k+32),end="")
    elif 97<=k<129:
        print(chr(k-32),end="")

# 18.알파벳 등장 갯수 구하기
alpha={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
       'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,
       'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
word=input().rstrip()

for i in word:
    alpha[i]+=1
for k,v in alpha.items():
    if v>=1:
        print(k,v)

